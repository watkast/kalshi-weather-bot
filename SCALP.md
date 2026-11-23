# Range-Scalp Bot

*Updated Mon Nov 23 13:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70038 | 61122 | 8916 (146) | 6 | $-18813.43 | -4.3% |
| **+10¢** | 52253 | 41839 | 10414 (189) | 6 | $-17471.19 | -5.3% |
| **+15¢** | 43785 | 32569 | 11216 (245) | 7 | $-15564.19 | -5.7% |
| **+20¢** | 38983 | 27180 | 11803 (310) | 8 | $-13927.72 | -5.7% |
| **+10¢ (15¢ stop)** | 85313 | 85123 | 190 (118) | 4 | $-31349.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 13:25 | +5 | DOGE | DOWN | 0.59 | open |  |
| 11-23 13:24 | +5 | SOL | UP | 0.61 | open |  |
| 11-23 13:24 | +10 stop | SOL | UP | 0.63 | open |  |
| 11-23 13:24 | +10 | SOL | UP | 0.63 | open |  |
| 11-23 13:24 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 11-23 13:24 | +10 | NEAR | DOWN | 0.63 | open |  |
| 11-23 13:24 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-23 13:24 | +10 stop | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 11-23 13:24 | +10 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-23 13:24 | +5 | ETH | DOWN | 0.60 | 0.69 | 0.58 |
| 11-23 13:23 | +15 | HYPE | DOWN | 0.69 | open |  |
| 11-23 13:23 | +10 | HYPE | DOWN | 0.69 | open |  |
| 11-23 13:23 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-23 13:23 | +10 stop | ZEC | UP | 0.68 | open |  |
| 11-23 13:23 | +10 stop | XRP | UP | 0.62 | 0.46 | -1.95 |
| 11-23 13:23 | +10 stop | DOGE | DOWN | 0.62 | open |  |
| 11-23 13:23 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-23 13:22 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 11-23 13:22 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 11-23 13:22 | +10 stop | ZEC | UP | 0.49 | 0.59 | 0.65 |
| 11-23 13:21 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-23 13:21 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 11-23 13:21 | +10 stop | BNB | UP | 0.47 | 0.26 | -2.42 |
| 11-23 13:21 | +5 | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 11-23 13:21 | +10 stop | DOGE | UP | 0.71 | 0.51 | -2.33 |
| 11-23 13:21 | +15 | DOGE | UP | 0.71 | open |  |
| 11-23 13:21 | +10 | DOGE | UP | 0.71 | open |  |
| 11-23 13:21 | +5 | DOGE | UP | 0.71 | 0.77 | 0.32 |
| 11-23 13:21 | +10 stop | NEAR | DOWN | 0.47 | 0.62 | 1.15 |
| 11-23 13:20 | +10 stop | BTC | DOWN | 0.70 | 0.52 | -2.13 |
| 11-23 13:20 | +15 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-23 13:20 | +10 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-23 13:20 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-23 13:20 | +10 stop | SOL | UP | 0.59 | 0.73 | 1.09 |
| 11-23 13:20 | +10 | SOL | UP | 0.59 | 0.73 | 1.09 |
| 11-23 13:20 | +5 | SOL | UP | 0.59 | 0.67 | 0.44 |
| 11-23 13:20 | +10 stop | HYPE | UP | 0.51 | 0.35 | -1.94 |
| 11-23 13:20 | +5 | HYPE | UP | 0.55 | open |  |
| 11-23 13:20 | +10 stop | BNB | DOWN | 0.63 | 0.43 | -2.35 |
| 11-23 13:20 | +10 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
