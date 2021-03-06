(function($) {
    $(document).ready(function($) {
      // you can now use jquery / javascript here...
      var dialog, form,

      WaistGirth = $( "#WaistGirth" ),
      HipsGirth = $( "#HipsGirth" ),
      Height = $( "#Height" ),
      BreastGirth = $( "#BreastGirth" ),
      ShoulderWidth = $( "#ShoulderWidth" ),
      tips = $( ".validateTips" ),
      detail_info = {},
      button_id = "";
      allFields = $( [] ).add( WaistGirth ).add( HipsGirth ).add( Height ).add( BreastGirth ).add( ShoulderWidth );

      function updateTips( t ) {
        tips
          .text( t )
          .addClass( "ui-state-highlight" );
        setTimeout(function() {
          tips.removeClass( "ui-state-highlight", 1500 );
        }, 500 );
      }


      function checkNumberic( value ) {
        if ( $.isNumeric(value) ) {
          return true;
        } else {
          updateTips("All value must be number.");
          return false;
        }
      }

      function fill() {
        if ( $( "#" + button_id ).prev().val() ) {
          detail_info = JSON.parse( $( "#" + button_id ).prev().val() );
        }
        WaistGirth.val(detail_info["WaistGirth"]);
        HipsGirth.val(detail_info["HipsGirth"]);
        Height.val(detail_info["Height"]);
        BreastGirth.val(detail_info["BreastGirth"]);
        ShoulderWidth.val(detail_info["ShoulderWidth"]);
      }

      function edit() {
        var valid = true;
        valid = valid && checkNumberic( WaistGirth.val() ) && checkNumberic( HipsGirth.val() ) 
                      && checkNumberic( Height.val() ) && checkNumberic( BreastGirth.val() ) && checkNumberic( ShoulderWidth.val() ); 

        if ( valid ) {
          detail_info["WaistGirth"] = Number(WaistGirth.val());
          detail_info["HipsGirth"] = Number(HipsGirth.val());
          detail_info["Height"] = Number(Height.val());
          detail_info["BreastGirth"] = Number(BreastGirth.val());
          detail_info["ShoulderWidth"] = Number(ShoulderWidth.val());
          $( "#" + button_id ).prev().val( JSON.stringify(detail_info) );
          dialog.dialog( "close" );
        }
        return valid;
      }
   
      dialog = $( "#detail-info-dialog" ).dialog({
        autoOpen: false,
        height: 550,
        width: 350,
        modal: true,
        buttons: {
          Ok: edit,
          Cancel: function() {
            dialog.dialog( "close" );
          }
        },
        close: function() {
          //form[ 0 ].reset();
          //allFields.removeClass( "ui-state-error" );
        },
        open: fill,
      });

      $( ".edit-detail-info-buttons" ).click(function(event){
          button_id = event.target.id;
          dialog.dialog( "open" );
      });
    });
})(django.jQuery);
