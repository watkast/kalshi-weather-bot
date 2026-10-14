# Range-Scalp Bot

*Updated Wed Oct 14 15:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16174 | 14010 | 2164 (27) | 5 | $-5126.78 | -5.0% |
| **+10¢** | 12221 | 9716 | 2505 (39) | 7 | $-4723.75 | -6.1% |
| **+15¢** | 10277 | 7586 | 2691 (58) | 8 | $-4238.47 | -6.6% |
| **+20¢** | 9142 | 6319 | 2823 (75) | 7 | $-3756.84 | -6.5% |
| **+10¢ (15¢ stop)** | 19921 | 19871 | 50 (29) | 0 | $-7656.65 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 15:53 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-14 15:53 | +5 | HYPE | DOWN | 0.69 | 0.78 | 0.62 |
| 10-14 15:53 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 10-14 15:53 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 10-14 15:53 | +10 stop | BTC | DOWN | 0.43 | 0.57 | 1.04 |
| 10-14 15:53 | +15 | BTC | DOWN | 0.44 | open |  |
| 10-14 15:53 | +10 | BTC | DOWN | 0.44 | 0.57 | 0.94 |
| 10-14 15:53 | +5 | BTC | DOWN | 0.45 | 0.57 | 0.84 |
| 10-14 15:52 | +10 stop | BTC | UP | 0.45 | 0.62 | 1.35 |
| 10-14 15:52 | +15 | BTC | UP | 0.45 | 0.62 | 1.35 |
| 10-14 15:52 | +10 | BTC | UP | 0.45 | 0.62 | 1.35 |
| 10-14 15:52 | +5 | BTC | UP | 0.45 | 0.62 | 1.35 |
| 10-14 15:52 | +10 stop | ETH | UP | 0.52 | 0.36 | -1.95 |
| 10-14 15:52 | +10 | ETH | UP | 0.52 | open |  |
| 10-14 15:52 | +5 | ETH | UP | 0.52 | 0.60 | 0.45 |
| 10-14 15:52 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.85 |
| 10-14 15:52 | +5 | HYPE | DOWN | 0.63 | 0.75 | 0.85 |
| 10-14 15:51 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-14 15:50 | +5 | HYPE | UP | 0.49 | 0.60 | 0.75 |
| 10-14 15:49 | +10 stop | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-14 15:49 | +20 | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 10-14 15:49 | +15 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-14 15:49 | +10 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-14 15:49 | +5 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-14 15:48 | +5 | DOGE | UP | 0.67 | open |  |
| 10-14 15:48 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 10-14 15:47 | +10 stop | HYPE | UP | 0.68 | 0.46 | -2.54 |
| 10-14 15:47 | +20 | HYPE | UP | 0.68 | open |  |
| 10-14 15:47 | +15 | HYPE | UP | 0.67 | open |  |
| 10-14 15:47 | +10 | HYPE | UP | 0.67 | open |  |
| 10-14 15:47 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 10-14 15:47 | +10 stop | NEAR | UP | 0.58 | 0.37 | -2.45 |
| 10-14 15:47 | +20 | NEAR | UP | 0.58 | open |  |
| 10-14 15:47 | +15 | NEAR | UP | 0.58 | open |  |
| 10-14 15:47 | +10 | NEAR | UP | 0.58 | open |  |
| 10-14 15:47 | +5 | NEAR | UP | 0.58 | open |  |
| 10-14 15:46 | +10 stop | DOGE | UP | 0.64 | 0.47 | -2.05 |
| 10-14 15:46 | +20 | DOGE | UP | 0.64 | open |  |
| 10-14 15:46 | +15 | DOGE | UP | 0.64 | open |  |
| 10-14 15:46 | +10 | DOGE | UP | 0.64 | open |  |
