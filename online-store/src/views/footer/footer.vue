<template>
  <footer>
    <!-- Begin Mailchimp Signup Form -->
    <div id="mc_embed_signup">
      <form action="https://qq.us18.list-manage.com/subscribe/post?u=0ea5ef0e2cecbea38f0a73658&amp;id=dc53881c62"
            method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate"
            target="_blank" novalidate>
        <div id="mc_embed_signup_scroll">
          <h2>Subscribe</h2>
          <div class="indicates-required"><span class="asterisk">*</span> indicates required</div>
          <div class="mc-field-group">
            <label for="mce-EMAIL">Email Address <span class="asterisk">*</span>
            </label>
            <input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
          </div>
          <div class="mc-field-group">
            <label for="mce-FNAME">First Name </label>
            <input type="text" value="" name="FNAME" class="" id="mce-FNAME">
          </div>
          <div class="mc-field-group">
            <label for="mce-LNAME">Last Name </label>
            <input type="text" value="" name="LNAME" class="" id="mce-LNAME">
          </div>
          <div class="mc-field-group size1of2">
            <label for="mce-BIRTHDAY-month">Birthday </label>
            <div class="datefield">
              <span class="subfield monthfield"><input class="birthday " type="text" pattern="[0-9]*" value=""
                                                       placeholder="MM" size="2" maxlength="2" name="BIRTHDAY[month]"
                                                       id="mce-BIRTHDAY-month"></span> /
              <span class="subfield dayfield"><input class="birthday " type="text" pattern="[0-9]*" value=""
                                                     placeholder="DD" size="2" maxlength="2" name="BIRTHDAY[day]"
                                                     id="mce-BIRTHDAY-day"></span>
              <span class="small-meta nowrap">( mm / dd )</span>
            </div>
          </div>
          <div id="mce-responses" class="clear">
            <div class="response" id="mce-error-response" style="display:none"></div>
            <div class="response" id="mce-success-response" style="display:none"></div>
          </div>
          <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
          <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text"
                                                                                    name="b_0ea5ef0e2cecbea38f0a73658_dc53881c62"
                                                                                    tabindex="-1" value=""></div>
          <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe"
                                    class="button"></div>
        </div>
      </form>
    </div>
  </footer>
</template>
<script>

  export default {
      mounted(){
          console.log($(document).height());
          console.log($(window).height());
          if ($(document).height() <= $(window).height()) {
              $('footer').css('position', 'absolute');
          }
      }
  }
</script>
<style scoped lang='scss'>
  footer {
    width: 100%;
    //position: relative;
    //bottom: 0px;
  }

  #mc_embed_signup {
    background: #e09bb7;
    clear: left;
    font: 14px Helvetica, Arial, sans-serif;
    text-align: center;
  }

  /* MailChimp Form Embed Code - Classic - 12/17/2015 v10.7 */
  #mc_embed_signup form {
    display: block;
    position: relative;
    text-align: left;
    padding: 10px 100px 10px 100px;
    background: #e09bb7;
    color: #FFffff;
    width: 500px;
    display: inline-block;
  }

  #mc_embed_signup h2 {
    font-weight: bold;
    padding: 0;
    margin-top: 15px;
    font-size: 1.4em;
  }

  #mc_embed_signup input {
    border: 1px solid #ABB0B2;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
  }

  #mc_embed_signup input[type=checkbox] {
    -webkit-appearance: checkbox;
  }

  #mc_embed_signup input[type=radio] {
    -webkit-appearance: radio;
  }

  #mc_embed_signup input:focus {
    border-color: #333;
  }

  #mc_embed_signup .button {
    clear: both;
    background-color: #4C1F59;
    border: 0 none;
    border-radius: 4px;
    transition: all 0.23s ease-in-out 0s;
    color: #FFFFFF;
    cursor: pointer;
    display: inline-block;
    font-size: 15px;
    font-weight: normal;
    height: 32px;
    line-height: 32px;
    margin: 0 5px 10px 0;
    padding: 0 22px;
    text-align: center;
    text-decoration: none;
    vertical-align: top;
    white-space: nowrap;
    width: auto;
  }

  #mc_embed_signup .button:hover {
    background-color: #4C1F59;
  }

  #mc_embed_signup .small-meta {
    font-size: 11px;
  }

  #mc_embed_signup .nowrap {
    white-space: nowrap;
  }

  #mc_embed_signup .mc-field-group {
    clear: left;
    position: relative;
    width: 96%;
    padding-bottom: 2%;
    min-height: 50px;
  }

  #mc_embed_signup .size1of2 {
    clear: none;
    float: left;
    display: inline-block;
    width: 46%;
    margin-right: 4%;
  }

  * html #mc_embed_signup .size1of2 {
    margin-right: 2%; /* Fix for IE6 double margins. */
  }

  #mc_embed_signup .mc-field-group label {
    display: block;
    margin-bottom: 3px;
  }

  #mc_embed_signup .mc-field-group input {
    display: block;
    width: 100%;
    padding: 8px 0;
    text-indent: 2%;
  }

  #mc_embed_signup .mc-field-group select {
    display: inline-block;
    width: 99%;
    padding: 5px 0;
    margin-bottom: 2px;
  }

  #mc_embed_signup .datefield, #mc_embed_signup .phonefield-us {
    padding: 5px 0;
  }

  #mc_embed_signup .datefield input, #mc_embed_signup .phonefield-us input {
    display: inline;
    width: 60px;
    margin: 0 2px;
    letter-spacing: 1px;
    text-align: center;
    padding: 5px 0 2px 0;
  }

  #mc_embed_signup .phonefield-us .phonearea input, #mc_embed_signup .phonefield-us .phonedetail1 input {
    width: 40px;
  }

  #mc_embed_signup .datefield .monthfield input, #mc_embed_signup .datefield .dayfield input {
    width: 30px;
  }

  #mc_embed_signup .datefield label, #mc_embed_signup .phonefield-us label {
    display: none;
  }

  #mc_embed_signup .indicates-required {
    text-align: right;
    font-size: 11px;
    margin-right: 4%;
  }

  #mc_embed_signup .asterisk {
    color: #e85c41;
    font-size: 150%;
    font-weight: normal;
    position: relative;
    top: 5px;
  }

  .clear {
    height: auto;
  }

  #mc_embed_signup .clear {
    clear: both;
  }

  #mc_embed_signup .mc-field-group.input-group ul {
    margin: 0;
    padding: 5px 0;
    list-style: none;
  }

  #mc_embed_signup .mc-field-group.input-group ul li {
    display: block;
    padding: 3px 0;
    margin: 0;
  }

  #mc_embed_signup .mc-field-group.input-group label {
    display: inline;
  }

  #mc_embed_signup .mc-field-group.input-group input {
    display: inline;
    width: auto;
    border: none;
  }

  #mc_embed_signup div#mce-responses {
    float: left;
    top: -1.4em;
    padding: 0em .5em 0em .5em;
    overflow: hidden;
    width: 90%;
    margin: 0 5%;
    clear: both;
  }

  #mc_embed_signup div.response {
    margin: 1em 0;
    padding: 1em .5em .5em 0;
    font-weight: bold;
    float: left;
    top: -1.5em;
    z-index: 1;
    width: 80%;
  }

  #mc_embed_signup #mce-error-response {
    display: none;
  }

  #mc_embed_signup #mce-success-response {
    color: #529214;
    display: none;
  }

  #mc_embed_signup label.error {
    display: block;
    float: none;
    width: auto;
    margin-left: 1.05em;
    text-align: left;
    padding: .5em 0;
  }

  #mc-embedded-subscribe {
    clear: both;
    width: auto;
    display: block;
    margin: 1em 0 1em 5%;
  }

  #mc_embed_signup #num-subscribers {
    font-size: 1.1em;
  }

  #mc_embed_signup #num-subscribers span {
    padding: .5em;
    border: 1px solid #ccc;
    margin-right: .5em;
    font-weight: bold;
  }

  #mc_embed_signup #mc-embedded-subscribe-form div.mce_inline_error {
    display: inline-block;
    margin: 2px 0 1em 0;
    padding: 5px 10px;
    background-color: rgba(255, 255, 255, 0.85);
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    font-size: 14px;
    font-weight: normal;
    z-index: 1;
    color: #e85c41;
  }

  #mc_embed_signup #mc-embedded-subscribe-form input.mce_inline_error {
    border: 2px solid #e85c41;
  }
</style>
