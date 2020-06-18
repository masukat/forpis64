function hamburger(){
    (function($) {
        var $body   = $('body');
        var $btn   = $('.toggle_btn');
        var $mask  = $('#mask');
        var open   = 'open';

        $btn.on( 'click', function() {
          if ( ! $body.hasClass( open ) ) {
            $body.addClass( open );
          } else {
            $body.removeClass( open );
          }
        });

        $mask.on('click', function() {
          $body.removeClass( open );
        });
      } )(jQuery);
}

function autoCompletion(){
    $('form').attr('autocomplete', 'off');
}


function AllChecked(){
    document.querySelectorAll('.checkbox input').forEach(function(input){
        input.checked = true;
    });
}

function checkbox_cell( obj,id ){
    var CELL = document.getElementById(id);
    var TABLE = CELL.parentNode.parentNode.parentNode;
    for(var i=0;TABLE.rows[i];i++) {
        TABLE.rows[i].cells[CELL.cellIndex].style.display = (obj.checked) ? '' : 'none';
    }
}


function rowspanizer(){
    /*!
    * jQuery Rowspanizer Plugin v0.1
    * https://github.com/marcosesperon/jquery.rowspanizer.js
    *
    * Copyright 2011, 2015 Marcos Esperón
    * Released under the MIT license
    *
    * https://github.com/jquery-boilerplate/boilerplate/
    */
    !function(t,n,e,i){"use strict";function a(n,e){this.element=n,this.settings=t.extend({},o,e),this._defaults=o,this._name=s,this.init()}var s="rowspanizer",o={vertical_align:"top"};t.extend(a.prototype,{init:function(){var n=this,e=t(this.element),i=[];e.find("tr").each(function(n,e){t(this).find("td").each(function(n,e){var a=t(e),s=a.html();if("undefined"!=typeof i[n]&&"dato"in i[n]&&i[n].dato==s){var o=i[n].elem.data("rowspan");("undefined"==o||isNaN(o))&&(o=1),i[n].elem.data("rowspan",parseInt(o)+1).addClass("rowspan-combine"),a.addClass("rowspan-remove")}else i[n]={dato:s,elem:a}})}),t(".rowspan-combine").each(function(e,i){var a=t(this);a.attr("rowspan",a.data("rowspan")).css({"vertical-align":n.settings.vertical_align})}),t(".rowspan-remove").remove()}}),t.fn[s]=function(n){return this.each(function(){t.data(this,"plugin_"+s)||t.data(this,"plugin_"+s,new a(this,n))})}}(jQuery,window,document);


    $('table').rowspanizer({columns: [2]});
}
