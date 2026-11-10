# Range-Scalp Bot

*Updated Tue Nov 10 09:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54501 | 47539 | 6962 (89) | 2 | $-14872.48 | -4.3% |
| **+10¢** | 40724 | 32599 | 8125 (117) | 4 | $-13826.71 | -5.4% |
| **+15¢** | 34137 | 25377 | 8760 (150) | 4 | $-12599.04 | -5.9% |
| **+20¢** | 30396 | 21208 | 9188 (198) | 5 | $-11003.98 | -5.8% |
| **+10¢ (15¢ stop)** | 66414 | 66304 | 110 (66) | 4 | $-24572.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 09:52 | +10 stop | NEAR | UP | 0.53 | open |  |
| 11-10 09:51 | +10 stop | DOGE | UP | 0.67 | open |  |
| 11-10 09:51 | +20 | DOGE | UP | 0.67 | open |  |
| 11-10 09:51 | +15 | DOGE | UP | 0.68 | open |  |
| 11-10 09:51 | +10 | DOGE | UP | 0.68 | open |  |
| 11-10 09:51 | +5 | DOGE | UP | 0.70 | 0.76 | 0.32 |
| 11-10 09:49 | +10 stop | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-10 09:49 | +20 | XRP | UP | 0.70 | open |  |
| 11-10 09:49 | +15 | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-10 09:49 | +10 | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-10 09:49 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 11-10 09:49 | +10 stop | NEAR | UP | 0.63 | 0.46 | -2.05 |
| 11-10 09:49 | +20 | NEAR | UP | 0.63 | open |  |
| 11-10 09:49 | +15 | NEAR | UP | 0.63 | open |  |
| 11-10 09:49 | +10 | NEAR | UP | 0.63 | open |  |
| 11-10 09:49 | +5 | NEAR | UP | 0.63 | open |  |
| 11-10 09:48 | +10 stop | ZEC | UP | 0.57 | open |  |
| 11-10 09:48 | +20 | ZEC | UP | 0.57 | open |  |
| 11-10 09:48 | +15 | ZEC | UP | 0.57 | open |  |
| 11-10 09:48 | +10 | ZEC | UP | 0.57 | open |  |
| 11-10 09:48 | +5 | ZEC | UP | 0.57 | open |  |
| 11-10 09:48 | +10 stop | ETH | UP | 0.70 | open |  |
| 11-10 09:48 | +20 | ETH | UP | 0.70 | open |  |
| 11-10 09:48 | +15 | ETH | UP | 0.70 | open |  |
| 11-10 09:48 | +10 | ETH | UP | 0.70 | open |  |
| 11-10 09:48 | +5 | ETH | UP | 0.70 | 0.76 | 0.32 |
| 11-10 09:40 | +10 stop | NEAR | UP | 0.38 | 0.54 | 1.25 |
| 11-10 09:39 | +10 stop | NEAR | DOWN | 0.61 | 0.43 | -2.18 |
| 11-10 09:39 | +10 stop | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 11-10 09:37 | +10 stop | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 11-10 09:37 | +10 stop | XRP | DOWN | 0.67 | 0.81 | 1.13 |
| 11-10 09:37 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-10 09:36 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 11-10 09:35 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-10 09:34 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-10 09:34 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 11-10 09:34 | +10 stop | XRP | DOWN | 0.70 | 0.55 | -1.83 |
| 11-10 09:34 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 11-10 09:33 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 09:32 | +5 | XRP | DOWN | 0.56 | 0.64 | 0.45 |
