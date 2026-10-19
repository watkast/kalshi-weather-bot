# Range-Scalp Bot

*Updated Mon Oct 19 12:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23969 | 20843 | 3126 (31) | 3 | $-7132.07 | -4.7% |
| **+10¢** | 18032 | 14427 | 3605 (45) | 3 | $-6363.90 | -5.6% |
| **+15¢** | 15109 | 11227 | 3882 (68) | 4 | $-5747.36 | -6.1% |
| **+20¢** | 13374 | 9312 | 4062 (87) | 5 | $-5120.58 | -6.1% |
| **+10¢ (15¢ stop)** | 29511 | 29460 | 51 (30) | 0 | $-11195.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 12:10 | +10 stop | ETH | UP | 0.54 | 0.64 | 0.65 |
| 10-19 12:10 | +20 | ETH | UP | 0.54 | open |  |
| 10-19 12:10 | +15 | ETH | UP | 0.55 | open |  |
| 10-19 12:10 | +10 | ETH | UP | 0.54 | 0.64 | 0.65 |
| 10-19 12:10 | +5 | ETH | UP | 0.54 | 0.62 | 0.45 |
| 10-19 12:09 | +10 stop | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-19 12:09 | +20 | BTC | UP | 0.71 | open |  |
| 10-19 12:09 | +15 | BTC | UP | 0.71 | 0.86 | 1.26 |
| 10-19 12:09 | +10 | BTC | UP | 0.71 | 0.86 | 1.26 |
| 10-19 12:09 | +5 | BTC | UP | 0.71 | 0.86 | 1.26 |
| 10-19 12:06 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 10-19 12:05 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-19 12:04 | +10 stop | ZEC | UP | 0.69 | 0.84 | 1.26 |
| 10-19 12:04 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 10-19 12:04 | +10 stop | NEAR | UP | 0.69 | 0.54 | -1.83 |
| 10-19 12:04 | +10 | XRP | UP | 0.64 | 0.89 | 2.26 |
| 10-19 12:04 | +5 | XRP | UP | 0.64 | 0.72 | 0.48 |
| 10-19 12:04 | +10 stop | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-19 12:04 | +20 | HYPE | UP | 0.65 | 0.92 | 2.44 |
| 10-19 12:04 | +15 | HYPE | UP | 0.65 | 0.81 | 1.33 |
| 10-19 12:04 | +10 | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-19 12:04 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 10-19 12:03 | +5 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-19 12:03 | +10 stop | BNB | UP | 0.52 | 0.65 | 0.96 |
| 10-19 12:03 | +10 stop | XRP | UP | 0.54 | 0.72 | 1.47 |
| 10-19 12:03 | +20 | XRP | UP | 0.53 | 0.89 | 3.35 |
| 10-19 12:03 | +15 | XRP | UP | 0.53 | 0.72 | 1.57 |
| 10-19 12:03 | +10 | XRP | UP | 0.53 | 0.63 | 0.65 |
| 10-19 12:03 | +5 | XRP | UP | 0.53 | 0.62 | 0.55 |
| 10-19 12:03 | +10 stop | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-19 12:03 | +20 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-19 12:03 | +15 | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-19 12:03 | +10 | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-19 12:03 | +5 | ETH | UP | 0.57 | 0.64 | 0.35 |
| 10-19 12:03 | +10 stop | BTC | DOWN | 0.56 | 0.41 | -1.85 |
| 10-19 12:02 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-19 12:01 | +10 stop | BNB | DOWN | 0.62 | 0.46 | -1.95 |
| 10-19 12:01 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-19 12:01 | +15 | BNB | DOWN | 0.56 | open |  |
| 10-19 12:01 | +10 | BNB | DOWN | 0.56 | open |  |
