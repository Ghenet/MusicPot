$(document).ready(function(){
  console.log('heree-----')
  var  key = 'AIzaSyDeYy4D1xgkXtBiLo6991ChSfODzHsrtMY';
  var playlistId = 'RDEMjYR1gmzilyT59I9huzoo0g'
  var URL = 'https://www.googleapis.com/youtube/v3/playlistItems';
    
  var options ={
   part :'snippet',
    key: key,
    maxResults: 5,
    playlistId: playlistId
  }

  loadVids();
  
  function loadVids(){
    $.getJSON(URL, options, function(data){
      console.log(data);
      var id = data.items[0].snippet.resourceId.videoId;
      mainVid(id);
      resultsloop(data);
    })
  }
  
  function mainVid(id){
    $('#video').html(`<iframe width="560" height="315" src="https://www.youtube.com/embed/${id}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`);
  }
    
    
  function resultsloop(data){

    $.each(data.items, function(i,item) {

      var thumb =item.snippet.thumbnails.medium.url;
      var title = item.snippet.title;
      var desc = item.snippet.description.substring(0,100); 
      var vid = item.snippet.resourceId.videoId;
    
      $('#testIdChangeLater').append(`
        <article class="item" data-key="${vid}">
          <img src="${thumb}" alt="" class="thumb">
          <div class="details">
            <h4>${title}</h4>
            <p>${desc}</p>
          </div>
        </article>
      `);
    });
  }
  
  $('main').on('click', 'article', function(){
    var id = $(this).attr('data-key');
    mainVid(id);
  });

  $('.songs').on('click', function(e) {
      e.preventDefault();
      // Get the new playlist ID (look into data attributes)
      var newId = $(this).attr('data-playlist-id')
      playlistId = newId
      // replace the old playlistId
      // call loadVids again
     

      var options ={
         part :'snippet',
         key: key,
         maxResults: 5,
         playlistId: playlistId
       }
     
       loadVids();
       
       function loadVids(){
         $.getJSON(URL, options, function(data){
           console.log(data);
           var id = data.items[2].snippet.resourceId.videoId;
           mainVid(id);
           resultsloop(data);
         })
       }
      //    function mainVid(id){
      //      $('#video').html(`<iframe width="560" height="315" src="https://www.youtube.com/embed/${id}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      //  `);
      //     }
        function resultsloop(data){
          $('#testIdChangeLater').empty()
          
          $.each(data.items, function(i,item){

            var thumb =item.snippet.thumbnails.medium.url;
            var title = item.snippet.title;
            var desc = item.snippet.description.substring(0,100); 
            var vid = item.snippet.resourceId.videoId;
            
            $('#testIdChangeLater').append(`
              <article class="item" data-key="${vid}">
                <img src="${thumb}" alt="" class="thumb">
                <div class="details">
                  <h4>${title}</h4>
                  <p>${desc}</p>
                </div>
              </article>
            `);
          });
          
          
          $('main').on('click','article', function(){
            var id = $(this).attr('data-key');
            mainVid(id);
          });
        }
      
     })


  });

  // PL6CTrxW12Bre4kny-OhqOEQwNjso0VKPc