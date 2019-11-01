var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var Proxy = require('./proxy');
var fs = require('fs')
var ROOT_PATH = path.resolve(__dirname);

module.exports = {
  devtool: 'source-map',
  entry: {
    // app: path.resolve(__dirname,'./src/main.js'),
    index: './src/main.js',
  },
  output: {
    path: __dirname + '/build',
    filename: "[name].[hash].entry.js",
    chunkFilename: "[name].[hash].min.js"
    //publicPath: '/build/'
  },
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      'vue$': 'vue/dist/vue.common.js'
    }
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    // new ExtractTextPlugin('style.css'),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'template.html',
      inject: true
    }),
    //new webpack.optimize.CommonsChunkPlugin({name:'vendor',filename:'vendor.bundle.js'})

    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery',
      'window.$': 'jquery',
    })
  ],
  /*
  externals: {
    jquery: 'window.$'
  }, */
  devServer: {
    //contentBase: './public',
    historyApiFallback: true,
    inline: true,
    hot: true,
    proxy: Proxy
  },
  module: {
    loaders: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        /*
        options: {
          loaders: {
            css: ExtractTextPlugin.extract({
              use: 'css-loader',
              fallback: 'vue-style-loader'
            })
          }
        } */
      },
      {
        test: /\.css$/,
        /*
        use: ExtractTextPlugin.extract({
          use: 'css-loader',
          fallback: 'style-loader'
        }) */
        loader: 'style-loader!css-loader'
        /*
        loader: 'style-loader!css-loader',
        options: {
          loaders: {
            css: ExtractTextPlugin.extract({
              use: 'css-loader'
            })
          }
        } */
      },
      {
        test: /\.scss$/,
        loader: 'style-loader!css-loader!sass-loader'
      },
      {
        test: /\.json$/,
        loader: 'json-loader'
      },
      {
        test: /\.(png|jpe?g|gif|svg|jgp)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: 'static/images/[name].[hash:7].[ext]'
        }
      },
      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: 'static/fonts/[name].[hash:7].[ext]'
        }
      },
      // {
      // 	test: /\.js$/,
      // 	loader: 'babel-loader',
      // 	query: {
      // 		compact: false
      // 	}
      // },
      {
        test: /iview.src.*?js$/,
        loader: 'babel-loader'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.exec\.js$/,
        use: ['script-loader']
      }
    ]
  },
}
