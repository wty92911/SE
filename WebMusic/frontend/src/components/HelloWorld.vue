<script setup>
  import {ref,onMounted} from 'vue'
  import {searchMusic} from '../api/api.js'
  defineProps({
    msg: {
      type: String,
      required: true
    }
  })
  const count = ref(1)
  const str = ref('')
  const urllist = ref([])
  function find(){
    searchMusic(str.value).then(
      (res) =>{
        console.log(res);
        urllist.value = res.data.musicUrl;
        
      }
    )
  }
  </script>
  
  <template>
    <div class="greetings">
      <h1 class="green">{{ msg }}</h1>
      <h3>
        <el-row display="margin-top:10px">
        <el-input v-model = "str" placeholder="请输入歌曲名"></el-input>
        <el-button type="primary" @click="find">查询</el-button>
      </el-row>
      <el-row>
        <el-table :data="urllist" style="width: 100%" >
        <el-table-column prop="url" label="url" min-width="100">
          <template v-slot="scope">
          {{scope.row.fields.url}}
          </template>
        </el-table-column>
        </el-table>
      </el-row>
      </h3>
    </div>
  </template>
  
  <style scoped>
  h1 {
    font-weight: 500;
    font-size: 2.6rem;
    top: -10px;
  }
  
  h3 {
    font-size: 1.2rem;
  }
  
  .greetings h1,
  .greetings h3 {
    text-align: center;
  }
  
  @media (min-width: 1024px) {
    .greetings h1,
    .greetings h3 {
      text-align: center;
    }
  }
  </style>
  