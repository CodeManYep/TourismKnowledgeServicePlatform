package cn.snnu.tksp.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.alibaba.fastjson.JSON;

import cn.snnu.tksp.service.TkspService;
import cn.snnu.tksp.util.FileUtil;
/**
 * 
 * 旅游知识服务平台首页功能展示
 * 关于 - 全国旅游知识地图可视化展示和说明
 * 搜索 - 语义搜索 + 简单问答
 * ...
 * @author zhangwz
 * 2019年10月7日下午5:14:26
 *
 */
@Controller
@RequestMapping("/tksp")
public class HomeController extends BaseController {
	private static final long serialVersionUID = 5431076596907150838L;

	@Resource
	TkspService tkspService;
	
	//进入 首页
	@RequestMapping(value = "/home", method = RequestMethod.GET)
	public String enterHome(HttpServletRequest request, 
							 HttpServletResponse response) throws Exception{
		System.out.println("------- home -------");
		
		return "home";
	}
	
	/**
	 * 获取Echarts配置项数据从统计文本中
	 * 
	 * 文本格式：名称	三元组数量	实体数量	关系数量
	 * @param request
	 * @param response
	 */
	@RequestMapping(value = "/getSeriesData", method = RequestMethod.GET)
	public void getAllStatics(HttpServletRequest request, 
							  HttpServletResponse response) {
		System.out.println("------- getAllStatics -------");
		List<String> statisticsList = new ArrayList<>();
		//获取类加载的根路径
		String pathName = this.getClass().getClassLoader().getResource("statisticText/allStatistics.txt").getPath();
		try {
			statisticsList = FileUtil.getAllStatics(pathName);
		} catch (IOException e) {
			e.printStackTrace();
		}
		String statisticsListStr = JSON.toJSONString(statisticsList);
		System.out.println(statisticsListStr);
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = null;
		try {
			out = response.getWriter();
			out.write(statisticsListStr);
			out.flush();
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	
	//进入 搜索 页面
	@RequestMapping(value = "/lookup", method = RequestMethod.GET)
	public String enterLookup(HttpServletRequest request, 
							 HttpServletResponse response) throws Exception{
		System.out.println("------- lookup -------");
		
		return "lookup";
	}
	
	/**
	 * 获取旅游知识图谱可视化展示需要的数据
	 *
	 * @param request
	 * @param response
	 * 2019年10月27日下午5:32:19
	 */
	@RequestMapping(value = "/getKnowledge", method = RequestMethod.GET)
	public void getDataandLink(HttpServletRequest request, 
							  HttpServletResponse response) {
		System.out.println("------- getDataandLink -------");
		//获取 实体名称 参数值
		String entityName = request.getParameter("entityName");
		String dataandLinkStr = "";
		try {
			entityName = new String(entityName.trim().getBytes("ISO-8859-1"), "UTF-8");
			//entityName = URLDecoder.decode(entityName , "UTF-8");
			System.out.println("entityName = " + entityName);
			
			//获取类加载的根路径
			String pathName = this.getClass().getClassLoader().getResource("statisticText/tourismKnowledge.txt").getPath();
		
			dataandLinkStr = FileUtil.getTourismKnowledge(pathName, entityName);
			//dataandLinkStr = JSON.toJSONString(dataandLinkStr);
			System.out.println(dataandLinkStr);
		} catch (IOException e) {
			e.printStackTrace();
		}
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = null;
		try {
			out = response.getWriter();
			out.write(dataandLinkStr);
			out.flush();
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	
	/**
	 * 统计知识库中不存在的实体并写入文本记录，供后续更新使用
	 * 基于用户查询量大小进行优先级排序，再做知识库更新操作
	 *
	 * @param request
	 * @param response
	 * 2019年11月1日下午4:33:46
	 * @throws URISyntaxException 
	 */
	@RequestMapping(value = "/addNewEntity", method = RequestMethod.GET)
	public void insertNewEntity(HttpServletRequest request, 
							  HttpServletResponse response) throws URISyntaxException {
		System.out.println("------- addNewEntity -------");
		//获取 实体名称 参数值
		String entityName = request.getParameter("entityName");
		try {
			entityName = new String(entityName.trim().getBytes("ISO-8859-1"), "UTF-8");
			//entityName = URLDecoder.decode(entityName , "UTF-8");
			System.out.println("entityName = " + entityName);
			
			//获取类加载的根路径
			String pathName = this.getClass().getClassLoader().getResource("/statisticText/newEitity.txt").getPath();
			//String pathName = this.getClass().getResource("/statisticText/newEitity.txt").getPath();
			//String pathName = "/" + request.getSession().getServletContext().getRealPath("/statisticText/newEitity.txt").replace("\\", "/");
			//String path = request.getContextPath();
			//path = path + "/src/statisticText/newEitity.txt";
			//String newPathName = this.getClass().getClassLoader().getResource("statisticText/newFinalEitity.txt").getPath();
			System.out.println("------- path -------");
			System.out.println(pathName);
			//插入操作
			FileUtil.addNewEntity(pathName, entityName);
			System.out.println("实体插入成功！！！");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	
	//初始化推荐搜索实体
	@RequestMapping(value = "/initRecEntity", method = RequestMethod.GET)
	public void getInitEntityList(HttpServletRequest request, 
			  HttpServletResponse response) throws URISyntaxException, IOException {
		System.out.println("------- initRecEntity -------");
		//推荐实体集合
		List<String> initRecommendEntityList = new ArrayList<>();
		String initRecEntListStr = "";	//推荐搜索
		try {
			//获取类加载的根路径 -存储推荐搜索的实体
			String pathName = this.getClass().getClassLoader().getResource("/statisticText/recommendedEitity.txt").getPath();
			System.out.println("------- path -------");
			System.out.println(pathName);
			//插入操作
			initRecommendEntityList = tkspService.staSearchedEntity(pathName, "0");
			initRecEntListStr = JSON.toJSONString(initRecommendEntityList);
			System.out.println("------- initRecEntList -------");
			System.out.println(initRecEntListStr);
			System.out.println("初始化搜索实体成功！！！");
			//获取类加载的根路径
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = null;
		try {
			out = response.getWriter();
			out.write(initRecEntListStr);
			out.flush();
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		//request.setAttribute("infoboxInfo", infoboxInfo);
		
		//response.sendRedirect("lookup");
	}
	
	/**
	 * 推荐搜索功能 + infobox数据
	 *
	 * @param request
	 * @param response
	 * @throws URISyntaxException
	 * 2019年11月3日下午4:32:16
	 * @throws IOException 
	 */
	@RequestMapping(value = "/getEntityList", method = RequestMethod.GET)
	public void getEntityList(HttpServletRequest request, 
			  HttpServletResponse response) throws URISyntaxException, IOException {
		System.out.println("------- getEntityList -------");
		String infoboxInfo = null;	//infobox信息
		//获取 实体名称 参数值
		String entityName = request.getParameter("entity");
		System.out.println("entityName = " + entityName);
		try {
			entityName = new String(entityName.trim().getBytes("ISO-8859-1"), "UTF-8");
			
			//获取类加载的根路径 -存储推荐搜索的实体
			String pathName = this.getClass().getClassLoader().getResource("/statisticText/recommendedEitity.txt").getPath();
			System.out.println("------- path -------");
			System.out.println(pathName);
			//插入操作,实体统计功能 - 这个功能冗余了，初始化的时候就可以获取到推荐的实体了
			tkspService.staSearchedEntity(pathName, entityName);
			System.out.println("实体搜索统计成功！！！");
			//获取类加载的根路径
			String path = this.getClass().getClassLoader().getResource("statisticText/tourismKnowledge.txt").getPath();
			infoboxInfo = tkspService.getInfoboxInfo(path, entityName);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = null;
		try {
			out = response.getWriter();
			out.write(infoboxInfo);
			out.flush();
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 获取top10实体排行数据，返回到前台可视化展示
	 *
	 * @param request
	 * @param response
	 * @throws URISyntaxException
	 * @throws IOException
	 * 2019年11月20日上午9:51:16
	 */
	@RequestMapping(value = "/entityRankData", method = RequestMethod.GET)
	public void getEntityRank(HttpServletRequest request, 
			  HttpServletResponse response) throws URISyntaxException, IOException {
		System.out.println("------- entityRankData -------");
		String entityRankData = null;	//entityRank数据
		try {
			//获取类加载的根路径 -存储推荐搜索的实体
			String pathName = this.getClass().getClassLoader().getResource("/statisticText/recommendedEitity.txt").getPath();
			System.out.println("------- path -------");
			System.out.println(pathName);
			//获取实体排名数据
			entityRankData = tkspService.getEntityRankData(pathName);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.println("------- entityRankData -------");
		System.out.println(entityRankData);
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = null;
		try {
			out = response.getWriter();
			out.write(entityRankData);
			out.flush();
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	//进入 实体排行榜 页面
	@RequestMapping(value = "/entityRank", method = RequestMethod.GET)
	public String enterEntityRank(HttpServletRequest request, 
							 HttpServletResponse response) throws Exception{
		System.out.println("------- entityRank -------");
		
		return "entityRank";
	}
	
	//进入 每周游报 页面
	@RequestMapping(value = "/weekTourism", method = RequestMethod.GET)
	public String enterWeekTourism(HttpServletRequest request, 
							 HttpServletResponse response) throws Exception{
		System.out.println("------- weekTourism -------");
		
		return "weekTourism";
	}
	
	//进入 文档 页面
	@RequestMapping(value = "/documentation", method = RequestMethod.GET)
	public String enterDocumentation(HttpServletRequest request, 
							 HttpServletResponse response) throws Exception{
		System.out.println("------- documentation -------");
		
		return "documentation";
	}
	
	//进入 开发团队 页面
	@RequestMapping(value = "/dteaminfo", method = RequestMethod.GET)
	public String enterDevelopTeamInfo(HttpServletRequest request, 
							 HttpServletResponse response) throws Exception{
		System.out.println("------- developTeamInfo -------");
		
		return "developTeamInfo";
	}
	
	//进入 API 页面
	@RequestMapping(value = "/api", method = RequestMethod.GET)
	public String enterAPI(HttpServletRequest request, 
							 HttpServletResponse response) throws Exception{
		System.out.println("------- api -------");
		
		return "API";
	}
	
	/**
	 * API接口调用
	 *
	 * @param request
	 * @param response
	 * @throws URISyntaxException
	 * @throws IOException
	 * 2019年11月30日下午6:22:22
	 */
	@RequestMapping(value = "/getEntityKnoList", method = RequestMethod.GET)
	public void getEntityKnoList(HttpServletRequest request, 
			  HttpServletResponse response) throws URISyntaxException, IOException {
		System.out.println("------- getEntityKnoList -------");
		String APIData = null;	//infobox信息
		//获取 实体名称 参数值
		String entityName = request.getParameter("entity");
		System.out.println("entityName = " + entityName);
		try {
			entityName = new String(entityName.trim().getBytes("ISO-8859-1"), "UTF-8");
			//获取类加载的根路径
			String path = this.getClass().getClassLoader().getResource("statisticText/tourismKnowledge.txt").getPath();
			APIData = tkspService.getInfoboxInfo(path, entityName);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = null;
		try {
			out = response.getWriter();
			out.write(APIData);
			out.flush();
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
