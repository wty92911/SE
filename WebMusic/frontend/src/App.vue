<script setup>
  import HelloWorld from './components/HelloWorld.vue'
  import TheWelcome from './components/TheWelcome.vue'
  </script>
  
  <template>
    <header>
      <img alt="WebMusic logo" class="logo" src="./assets/logo.png" />
      
      
    </header>
    <main><HelloWorld msg="Find Music" /></main>
    
      
    
  </template>
  
  <style scoped>
  header {
    line-height: 1.5;
  }
  
  .logo {
    display: block;
    margin: 0 auto 2rem;
    width:50%;
  }
  
  @media (min-width: 1024px) {
    header {
    line-height: 1.5;
  }
  
    .logo {
    display: block;
    margin: 0 auto 2rem;
    width:50%;
  }
  
    header .wrapper {
      display: flex;
      place-items: flex-start;
      flex-wrap: wrap;
    }
  }
  </style>
  