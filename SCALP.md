# Range-Scalp Bot

*Updated Thu Nov 26 13:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72720 | 63473 | 9247 (158) | 5 | $-19350.70 | -4.2% |
| **+10¢** | 54226 | 43426 | 10800 (203) | 6 | $-17966.38 | -5.3% |
| **+15¢** | 45403 | 33768 | 11635 (261) | 7 | $-16075.32 | -5.6% |
| **+20¢** | 40413 | 28163 | 12250 (327) | 8 | $-14457.19 | -5.7% |
| **+10¢ (15¢ stop)** | 88563 | 88354 | 209 (128) | 5 | $-32602.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 13:25 | +5 | NEAR | UP | 0.61 | open |  |
| 11-26 13:25 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-26 13:25 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-26 13:25 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 11-26 13:25 | +10 stop | BTC | UP | 0.56 | open |  |
| 11-26 13:24 | +10 stop | NEAR | UP | 0.62 | open |  |
| 11-26 13:24 | +20 | NEAR | UP | 0.62 | open |  |
| 11-26 13:24 | +15 | NEAR | UP | 0.62 | open |  |
| 11-26 13:24 | +10 | NEAR | UP | 0.62 | open |  |
| 11-26 13:24 | +5 | NEAR | UP | 0.62 | 0.68 | 0.27 |
| 11-26 13:24 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 11-26 13:23 | +10 stop | ETH | UP | 0.65 | open |  |
| 11-26 13:23 | +10 stop | BTC | UP | 0.69 | 0.53 | -1.93 |
| 11-26 13:23 | +10 stop | BNB | UP | 0.71 | 0.47 | -2.73 |
| 11-26 13:22 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 11-26 13:22 | +10 stop | DOGE | UP | 0.54 | 0.39 | -1.85 |
| 11-26 13:22 | +10 stop | SOL | UP | 0.56 | 0.40 | -1.95 |
| 11-26 13:22 | +5 | SOL | UP | 0.56 | open |  |
| 11-26 13:21 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 11-26 13:21 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 11-26 13:20 | +10 stop | XRP | UP | 0.67 | 0.79 | 0.92 |
| 11-26 13:20 | +5 | SOL | DOWN | 0.59 | 0.65 | 0.27 |
| 11-26 13:19 | +10 stop | BNB | UP | 0.55 | 0.66 | 0.76 |
| 11-26 13:19 | +5 | BTC | DOWN | 0.57 | open |  |
| 11-26 13:18 | +5 | ZEC | DOWN | 0.59 | 0.67 | 0.47 |
| 11-26 13:17 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.03 |
| 11-26 13:17 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-26 13:17 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-26 13:17 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-26 13:17 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-26 13:17 | +5 | ZEC | DOWN | 0.56 | 0.62 | 0.25 |
| 11-26 13:17 | +10 stop | DOGE | DOWN | 0.63 | 0.43 | -2.35 |
| 11-26 13:17 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-26 13:17 | +15 | DOGE | DOWN | 0.63 | 0.82 | 1.62 |
| 11-26 13:17 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-26 13:17 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 11-26 13:16 | +10 stop | BTC | DOWN | 0.57 | 0.35 | -2.54 |
| 11-26 13:16 | +20 | BTC | DOWN | 0.57 | open |  |
| 11-26 13:16 | +15 | BTC | DOWN | 0.57 | open |  |
| 11-26 13:16 | +10 | BTC | DOWN | 0.57 | open |  |
