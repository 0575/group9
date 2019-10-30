<template>
  <div id="wrapper">
    <current-loc :curLoc="curLoc"></current-loc>
    <div class="main cle">
      <list-nav :currentCategoryName="currentCategoryName" :cateMenu="cateMenu" :proNum="proNum" :isObject="isObject"
                @on-change="changeMenu"></list-nav>
      <div class="maincon">
        <price-range :priceRange="priceRange" @on-change="changePrice"></price-range>
        <list-sort @on-sort="changeSort" :proNum="proNum"></list-sort>
        <div class="list-detail">
          <product-list :listData="listData"></product-list>
          <Page pre-text="Previous Page" next-text="Next Page" end-show="false" :page="curPage" :total-page='totalPage'
                @pagefn="pagefn"></Page>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
    // Product List
    import productList from './product-list/productList';
    // Left List Nav
    import listNav from './list-nav/listNav';
    // List Sort
    import listSort from './list-sort/listSort';
    // Page turning
    import page from './page/page';
    // Current page
    import currentLoc from './current-loc/current-loc';
    // Price range
    import priceRange from './price-range/priceRange';

    import {getCategory, getGoods} from '../../api/api'

    export default {
        data() {
            return {
                curPage: 1,
                top_category: '',
                listData: [],
                cateMenu: {},
                isObject: true,
                ordering: '-add_time',
                proNum: 0,
                curLoc: [],
                priceRange: [],
                pricemin: '',
                pricemax: '',
                pageType: 'list',
                searchWord: '',
                currentCategoryName: ''
            };
        },
        components: {
            'product-list': productList,
            'list-nav': listNav,
            'list-sort': listSort,
            'Page': page,
            'current-loc': currentLoc,
            'price-range': priceRange

        },
        props: {},
        created() {
            this.getAllData();
        },
        watch: {
            "$route": "getAllData"
        },
        computed: {
            totalPage() {
                return Math.ceil(this.proNum / 12)
            }
        },
        methods: {
            getAllData() {
                console.log(this.$route.params)
                if (this.$route.params.id) {
                    this.top_category = this.$route.params.id;
                    this.getMenu(this.top_category);
                } else {
                    this.getMenu(null);
                    this.pageType = 'search'
                    this.searchWord = this.$route.params.keyword;
                }

                this.getCurLoc();
                this.getListData();
                this.getPriceRange();
            },
            getListData() {
                if (this.pageType == 'search') {
                    getGoods({
                        search: this.searchWord,
                    }).then((response) => {
                        this.listData = response.data.results;
                        this.proNum = response.data.count;
                    }).catch(function (error) {
                        console.log(error);
                    });
                } else {
                    getGoods({
                        page: this.curPage,
                        top_category: this.top_category,
                        ordering: this.ordering,
                        pricemin: this.pricemin,
                        pricemax: this.pricemax
                    }).then((response) => {

                        this.listData = response.data.results;
                        this.proNum = response.data.count;
                    }).catch(function (error) {
                        console.log(error);
                    });
                }

            },
            getMenu(id) {
                if (id != null) {
                    getCategory({
                        id: this.$route.params.id
                    }).then((response) => {
                        this.cateMenu = response.data.sub_cat;
                        this.currentCategoryName = response.data.name
                    }).catch(function (error) {
                        console.log(error);
                    });
                } else {
                    getCategory({}).then((response) => {
                        this.cateMenu = response.data;
                        this.isObject = false
                    }).catch(function (error) {
                        console.log(error);
                    });
                }

            },

            getCurLoc() {
                this.$http.post('/currentLoc', {
                    params: {
                        proType: this.type,
                    }
                }).then((response) => {

                    this.curLoc = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            getPriceRange() {
                this.$http.post('/priceRange', {
                    params: {
                        proType: this.type,
                    }
                }).then((response) => {

                    this.priceRange = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            changeSort(type) {

                this.ordering = type;
                this.getListData();

            },
            changePrice(data) {
                this.pricemin = data.min;
                this.pricemax = data.max;
                this.getListData();
            },
            changeMenu(id) {
                this.top_category = id;
                this.getCurLoc();
                this.getMenu(id);
                this.getListData();
            },
            pagefn(value) {
                this.curPage = value.page;
                this.getListData()
            }
        }
    }
</script>
<style lang='scss'>
  .maincon {
    width: 970px;
    float: right;
  }
</style>
