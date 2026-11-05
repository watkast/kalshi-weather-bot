# Range-Scalp Bot

*Updated Thu Nov 05 21:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48756 | 42497 | 6259 (74) | 5 | $-13774.49 | -4.5% |
| **+10¢** | 36394 | 29115 | 7279 (100) | 4 | $-12656.03 | -5.5% |
| **+15¢** | 30479 | 22639 | 7840 (129) | 4 | $-11544.43 | -6.0% |
| **+20¢** | 27078 | 18860 | 8218 (168) | 4 | $-10220.34 | -6.0% |
| **+10¢ (15¢ stop)** | 59412 | 59317 | 95 (57) | 0 | $-21994.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 21:51 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-05 21:50 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-05 21:50 | +10 stop | NEAR | DOWN | 0.68 | 0.81 | 1.03 |
| 11-05 21:50 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-05 21:49 | +10 stop | ETH | UP | 0.51 | 0.35 | -1.94 |
| 11-05 21:49 | +10 | ETH | UP | 0.51 | open |  |
| 11-05 21:49 | +5 | ETH | UP | 0.51 | open |  |
| 11-05 21:49 | +10 stop | BNB | DOWN | 0.57 | 0.70 | 0.97 |
| 11-05 21:49 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-05 21:48 | +10 stop | SOL | UP | 0.58 | 0.37 | -2.45 |
| 11-05 21:47 | +10 stop | NEAR | UP | 0.61 | 0.40 | -2.44 |
| 11-05 21:47 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-05 21:47 | +5 | ZEC | UP | 0.71 | open |  |
| 11-05 21:47 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 11-05 21:47 | +5 | NEAR | UP | 0.61 | open |  |
| 11-05 21:47 | +10 stop | BTC | UP | 0.61 | 0.41 | -2.34 |
| 11-05 21:47 | +20 | BTC | UP | 0.61 | open |  |
| 11-05 21:47 | +15 | BTC | UP | 0.61 | open |  |
| 11-05 21:47 | +10 | BTC | UP | 0.61 | open |  |
| 11-05 21:47 | +5 | BTC | UP | 0.61 | open |  |
| 11-05 21:47 | +5 | XRP | DOWN | 0.62 | 0.70 | 0.48 |
| 11-05 21:47 | +10 stop | HYPE | UP | 0.56 | 0.40 | -1.95 |
| 11-05 21:47 | +20 | HYPE | UP | 0.55 | open |  |
| 11-05 21:47 | +15 | HYPE | UP | 0.55 | open |  |
| 11-05 21:47 | +10 | HYPE | UP | 0.55 | open |  |
| 11-05 21:47 | +5 | HYPE | UP | 0.55 | open |  |
| 11-05 21:46 | +10 stop | XRP | DOWN | 0.61 | 0.81 | 1.70 |
| 11-05 21:46 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-05 21:46 | +15 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-05 21:46 | +10 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-05 21:46 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 11-05 21:46 | +10 stop | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-05 21:46 | +20 | ETH | UP | 0.61 | open |  |
| 11-05 21:46 | +15 | ETH | UP | 0.61 | open |  |
| 11-05 21:46 | +10 | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-05 21:46 | +5 | ETH | UP | 0.61 | 0.68 | 0.37 |
| 11-05 21:46 | +10 stop | ZEC | UP | 0.61 | 0.35 | -2.93 |
| 11-05 21:46 | +20 | ZEC | UP | 0.61 | open |  |
| 11-05 21:46 | +15 | ZEC | UP | 0.61 | open |  |
| 11-05 21:46 | +10 | ZEC | UP | 0.61 | open |  |
