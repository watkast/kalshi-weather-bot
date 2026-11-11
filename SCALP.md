# Range-Scalp Bot

*Updated Wed Nov 11 02:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55283 | 48217 | 7066 (94) | 9 | $-15068.22 | -4.3% |
| **+10¢** | 41297 | 33053 | 8244 (124) | 9 | $-14011.44 | -5.4% |
| **+15¢** | 34623 | 25737 | 8886 (158) | 9 | $-12752.58 | -5.9% |
| **+20¢** | 30827 | 21505 | 9322 (207) | 9 | $-11152.34 | -5.8% |
| **+10¢ (15¢ stop)** | 67339 | 67221 | 118 (73) | 0 | $-24831.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 02:53 | +10 stop | NEAR | DOWN | 0.51 | 0.66 | 1.16 |
| 11-11 02:53 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.14 |
| 11-11 02:52 | +10 stop | NEAR | DOWN | 0.70 | 0.54 | -1.93 |
| 11-11 02:51 | +10 stop | HYPE | UP | 0.71 | 0.49 | -2.53 |
| 11-11 02:51 | +20 | HYPE | UP | 0.71 | open |  |
| 11-11 02:51 | +15 | HYPE | UP | 0.71 | open |  |
| 11-11 02:51 | +10 | HYPE | UP | 0.71 | open |  |
| 11-11 02:51 | +5 | HYPE | UP | 0.71 | open |  |
| 11-11 02:51 | +10 stop | BNB | DOWN | 0.53 | 0.68 | 1.16 |
| 11-11 02:51 | +10 stop | NEAR | UP | 0.57 | 0.41 | -1.95 |
| 11-11 02:51 | +20 | NEAR | UP | 0.57 | open |  |
| 11-11 02:51 | +15 | NEAR | UP | 0.57 | open |  |
| 11-11 02:51 | +10 | NEAR | UP | 0.60 | open |  |
| 11-11 02:51 | +5 | NEAR | UP | 0.60 | open |  |
| 11-11 02:51 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 11-11 02:51 | +10 stop | ZEC | DOWN | 0.69 | 0.90 | 1.89 |
| 11-11 02:51 | +10 stop | BTC | UP | 0.57 | 0.38 | -2.25 |
| 11-11 02:50 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-11 02:49 | +5 | BNB | UP | 0.71 | open |  |
| 11-11 02:49 | +5 | XRP | UP | 0.67 | open |  |
| 11-11 02:48 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 11-11 02:48 | +5 | ZEC | UP | 0.67 | open |  |
| 11-11 02:48 | +5 | DOGE | UP | 0.56 | open |  |
| 11-11 02:48 | +5 | XRP | UP | 0.55 | 0.62 | 0.35 |
| 11-11 02:47 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 11-11 02:46 | +10 stop | ZEC | UP | 0.68 | 0.36 | -3.53 |
| 11-11 02:46 | +20 | ZEC | UP | 0.68 | open |  |
| 11-11 02:46 | +15 | ZEC | UP | 0.68 | open |  |
| 11-11 02:46 | +10 | ZEC | UP | 0.68 | open |  |
| 11-11 02:46 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 11-11 02:46 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 11-11 02:46 | +20 | BTC | UP | 0.70 | open |  |
| 11-11 02:46 | +15 | BTC | UP | 0.70 | open |  |
| 11-11 02:46 | +10 | BTC | UP | 0.70 | open |  |
| 11-11 02:46 | +5 | BTC | UP | 0.70 | open |  |
| 11-11 02:46 | +10 stop | XRP | UP | 0.59 | 0.34 | -2.83 |
| 11-11 02:46 | +20 | XRP | UP | 0.59 | open |  |
| 11-11 02:46 | +15 | XRP | UP | 0.59 | open |  |
| 11-11 02:46 | +10 | XRP | UP | 0.59 | open |  |
| 11-11 02:46 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
