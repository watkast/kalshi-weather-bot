# Range-Scalp Bot

*Updated Tue Nov 10 23:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55038 | 47999 | 7039 (94) | 1 | $-15043.48 | -4.3% |
| **+10¢** | 41128 | 32920 | 8208 (124) | 2 | $-13933.29 | -5.4% |
| **+15¢** | 34480 | 25636 | 8844 (158) | 3 | $-12649.62 | -5.8% |
| **+20¢** | 30693 | 21414 | 9279 (207) | 3 | $-11067.52 | -5.8% |
| **+10¢ (15¢ stop)** | 67052 | 66934 | 118 (73) | 1 | $-24779.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 23:24 | +5 | HYPE | UP | 0.62 | 0.75 | 0.99 |
| 11-10 23:23 | +10 stop | BTC | UP | 0.71 | open |  |
| 11-10 23:23 | +20 | BTC | UP | 0.71 | open |  |
| 11-10 23:23 | +15 | BTC | UP | 0.71 | open |  |
| 11-10 23:23 | +10 | BTC | UP | 0.71 | open |  |
| 11-10 23:23 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 11-10 23:23 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-10 23:23 | +15 | HYPE | UP | 0.63 | open |  |
| 11-10 23:23 | +10 | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 11-10 23:23 | +5 | HYPE | UP | 0.63 | 0.71 | 0.48 |
| 11-10 23:20 | +10 | HYPE | UP | 0.64 | 0.77 | 0.97 |
| 11-10 23:20 | +5 | HYPE | UP | 0.64 | 0.73 | 0.58 |
| 11-10 23:20 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-10 23:19 | +10 stop | HYPE | UP | 0.57 | 0.73 | 1.25 |
| 11-10 23:19 | +20 | HYPE | UP | 0.58 | open |  |
| 11-10 23:19 | +15 | HYPE | UP | 0.56 | 0.73 | 1.38 |
| 11-10 23:19 | +10 | HYPE | UP | 0.56 | 0.67 | 0.76 |
| 11-10 23:19 | +5 | HYPE | UP | 0.56 | 0.67 | 0.76 |
| 11-10 23:18 | +10 stop | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 11-10 23:18 | +20 | NEAR | UP | 0.70 | 0.92 | 1.97 |
| 11-10 23:18 | +15 | NEAR | UP | 0.70 | 0.88 | 1.57 |
| 11-10 23:18 | +10 | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 11-10 23:18 | +5 | NEAR | UP | 0.70 | 0.78 | 0.52 |
| 11-10 23:18 | +10 stop | BTC | UP | 0.66 | 0.80 | 1.12 |
| 11-10 23:18 | +20 | BTC | UP | 0.65 | 0.86 | 1.85 |
| 11-10 23:18 | +15 | BTC | UP | 0.65 | 0.80 | 1.22 |
| 11-10 23:18 | +10 | BTC | UP | 0.65 | 0.80 | 1.22 |
| 11-10 23:18 | +5 | BTC | UP | 0.65 | 0.71 | 0.29 |
| 11-10 23:18 | +10 stop | DOGE | DOWN | 0.57 | 0.36 | -2.45 |
| 11-10 23:18 | +10 | DOGE | DOWN | 0.57 | open |  |
| 11-10 23:18 | +5 | DOGE | DOWN | 0.57 | open |  |
| 11-10 23:18 | +10 stop | XRP | UP | 0.70 | 0.52 | -2.13 |
| 11-10 23:18 | +20 | XRP | UP | 0.70 | 0.91 | 1.93 |
| 11-10 23:18 | +15 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 11-10 23:18 | +10 | XRP | UP | 0.70 | 0.82 | 0.94 |
| 11-10 23:18 | +5 | XRP | UP | 0.70 | 0.79 | 0.63 |
| 11-10 23:17 | +5 | BNB | UP | 0.55 | 0.62 | 0.35 |
| 11-10 23:17 | +5 | DOGE | UP | 0.57 | 0.62 | 0.18 |
| 11-10 23:16 | +10 stop | DOGE | DOWN | 0.48 | 0.61 | 0.95 |
| 11-10 23:16 | +20 | DOGE | DOWN | 0.48 | open |  |
