# Range-Scalp Bot

*Updated Sun Nov 01 01:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43019 | 37501 | 5518 (62) | 1 | $-12197.50 | -4.5% |
| **+10¢** | 32080 | 25704 | 6376 (84) | 1 | $-10929.55 | -5.4% |
| **+15¢** | 26833 | 19958 | 6875 (112) | 2 | $-10028.71 | -6.0% |
| **+20¢** | 23834 | 16632 | 7202 (145) | 4 | $-8860.76 | -5.9% |
| **+10¢ (15¢ stop)** | 52472 | 52389 | 83 (48) | 1 | $-19874.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 01:21 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.74 |
| 11-01 01:21 | +15 | XRP | UP | 0.65 | open |  |
| 11-01 01:21 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-01 01:20 | +10 stop | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 11-01 01:20 | +10 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 11-01 01:20 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 11-01 01:20 | +10 stop | NEAR | UP | 0.69 | 0.94 | 2.25 |
| 11-01 01:20 | +20 | NEAR | UP | 0.69 | 0.94 | 2.25 |
| 11-01 01:20 | +15 | NEAR | UP | 0.69 | 0.94 | 2.25 |
| 11-01 01:20 | +10 | NEAR | UP | 0.69 | 0.94 | 2.25 |
| 11-01 01:20 | +5 | NEAR | UP | 0.69 | 0.94 | 2.25 |
| 11-01 01:20 | +10 stop | XRP | DOWN | 0.68 | 0.35 | -3.62 |
| 11-01 01:20 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-01 01:17 | +5 | SOL | UP | 0.67 | 0.75 | 0.50 |
| 11-01 01:17 | +5 | DOGE | UP | 0.70 | 0.78 | 0.52 |
| 11-01 01:17 | +5 | HYPE | UP | 0.71 | 0.77 | 0.32 |
| 11-01 01:16 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-01 01:16 | +20 | XRP | DOWN | 0.55 | open |  |
| 11-01 01:16 | +15 | XRP | DOWN | 0.55 | 0.71 | 1.27 |
| 11-01 01:16 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-01 01:16 | +5 | XRP | DOWN | 0.56 | 0.65 | 0.56 |
| 11-01 01:16 | +10 stop | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-01 01:16 | +20 | HYPE | UP | 0.62 | 0.85 | 2.04 |
| 11-01 01:16 | +15 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-01 01:16 | +10 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-01 01:16 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 11-01 01:16 | +10 stop | SOL | UP | 0.60 | 0.75 | 1.19 |
| 11-01 01:16 | +20 | SOL | UP | 0.60 | 0.82 | 1.92 |
| 11-01 01:16 | +15 | SOL | UP | 0.60 | 0.75 | 1.19 |
| 11-01 01:16 | +10 | SOL | UP | 0.61 | 0.75 | 1.09 |
| 11-01 01:16 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-01 01:16 | +10 stop | BTC | UP | 0.60 | open |  |
| 11-01 01:16 | +20 | BTC | UP | 0.60 | open |  |
| 11-01 01:16 | +15 | BTC | UP | 0.60 | open |  |
| 11-01 01:16 | +10 | BTC | UP | 0.60 | open |  |
| 11-01 01:16 | +5 | BTC | UP | 0.61 | 0.66 | 0.17 |
| 11-01 01:16 | +10 stop | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 11-01 01:16 | +20 | DOGE | UP | 0.66 | open |  |
| 11-01 01:16 | +15 | DOGE | UP | 0.66 | 0.82 | 1.33 |
| 11-01 01:16 | +10 | DOGE | UP | 0.66 | 0.78 | 0.91 |
