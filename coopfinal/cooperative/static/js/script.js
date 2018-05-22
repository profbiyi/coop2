
new Vue({
   el:'#app',
   data:{
     amount:'',
     tenure:''

   },
    computed: {
                install: function(){
                    return this.amount /this.tenure;
                }
            }



})












