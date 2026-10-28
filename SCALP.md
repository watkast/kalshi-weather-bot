# Range-Scalp Bot

*Updated Wed Oct 28 21:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38547 | 33637 | 4910 (48) | 4 | $-10837.15 | -4.5% |
| **+10¢** | 28749 | 23079 | 5670 (70) | 5 | $-9604.28 | -5.3% |
| **+15¢** | 24050 | 17962 | 6088 (95) | 6 | $-8540.26 | -5.7% |
| **+20¢** | 21336 | 14962 | 6374 (120) | 6 | $-7461.71 | -5.6% |
| **+10¢ (15¢ stop)** | 47155 | 47088 | 67 (35) | 0 | $-17894.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 21:27 | +10 stop | SOL | UP | 0.55 | 0.69 | 1.07 |
| 10-28 21:27 | +20 | SOL | UP | 0.56 | open |  |
| 10-28 21:27 | +15 | SOL | UP | 0.56 | open |  |
| 10-28 21:27 | +10 | SOL | UP | 0.56 | 0.69 | 0.97 |
| 10-28 21:27 | +5 | SOL | UP | 0.56 | 0.69 | 0.97 |
| 10-28 21:26 | +5 | XRP | UP | 0.63 | open |  |
| 10-28 21:25 | +10 stop | HYPE | DOWN | 0.59 | 0.87 | 2.51 |
| 10-28 21:25 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.33 |
| 10-28 21:25 | +10 stop | NEAR | UP | 0.53 | 0.34 | -2.24 |
| 10-28 21:25 | +20 | NEAR | UP | 0.53 | open |  |
| 10-28 21:25 | +15 | NEAR | UP | 0.53 | open |  |
| 10-28 21:25 | +10 | NEAR | UP | 0.53 | open |  |
| 10-28 21:25 | +5 | NEAR | UP | 0.53 | open |  |
| 10-28 21:25 | +10 stop | DOGE | UP | 0.57 | 0.20 | -4.00 |
| 10-28 21:25 | +20 | DOGE | UP | 0.57 | open |  |
| 10-28 21:25 | +15 | DOGE | UP | 0.57 | open |  |
| 10-28 21:25 | +10 | DOGE | UP | 0.58 | open |  |
| 10-28 21:25 | +5 | DOGE | UP | 0.60 | open |  |
| 10-28 21:25 | +10 stop | XRP | UP | 0.71 | 0.32 | -4.21 |
| 10-28 21:25 | +20 | XRP | UP | 0.71 | open |  |
| 10-28 21:25 | +15 | XRP | UP | 0.68 | open |  |
| 10-28 21:25 | +10 | XRP | UP | 0.67 | open |  |
| 10-28 21:25 | +5 | XRP | UP | 0.67 | 0.74 | 0.40 |
| 10-28 21:24 | +10 stop | BTC | UP | 0.62 | 0.47 | -1.85 |
| 10-28 21:24 | +10 | BTC | UP | 0.62 | open |  |
| 10-28 21:24 | +5 | BTC | UP | 0.62 | open |  |
| 10-28 21:23 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.88 |
| 10-28 21:23 | +20 | HYPE | UP | 0.68 | open |  |
| 10-28 21:23 | +10 | HYPE | UP | 0.68 | open |  |
| 10-28 21:23 | +5 | HYPE | UP | 0.68 | 0.76 | 0.51 |
| 10-28 21:21 | +5 | BTC | UP | 0.68 | 0.75 | 0.40 |
| 10-28 21:20 | +10 stop | HYPE | UP | 0.66 | 0.81 | 1.20 |
| 10-28 21:20 | +15 | HYPE | UP | 0.66 | open |  |
| 10-28 21:20 | +10 | HYPE | UP | 0.66 | 0.81 | 1.20 |
| 10-28 21:20 | +5 | HYPE | UP | 0.66 | 0.75 | 0.56 |
| 10-28 21:18 | +10 stop | HYPE | UP | 0.60 | 0.79 | 1.57 |
| 10-28 21:18 | +20 | HYPE | UP | 0.60 | 0.81 | 1.78 |
| 10-28 21:18 | +15 | HYPE | UP | 0.60 | 0.79 | 1.57 |
| 10-28 21:18 | +10 | HYPE | UP | 0.60 | 0.79 | 1.57 |
| 10-28 21:18 | +5 | HYPE | UP | 0.60 | 0.69 | 0.54 |
