# Range-Scalp Bot

*Updated Sat Oct 24 23:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32223 | 28096 | 4127 (40) | 1 | $-9199.41 | -4.5% |
| **+10¢** | 24121 | 19340 | 4781 (58) | 2 | $-8249.30 | -5.4% |
| **+15¢** | 20200 | 15058 | 5142 (81) | 2 | $-7385.96 | -5.8% |
| **+20¢** | 17894 | 12513 | 5381 (103) | 3 | $-6541.85 | -5.8% |
| **+10¢ (15¢ stop)** | 39596 | 39537 | 59 (32) | 1 | $-15139.68 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 23:31 | +5 | NEAR | UP | 0.60 | 0.69 | 0.58 |
| 10-24 23:31 | +10 stop | HYPE | UP | 0.71 | open |  |
| 10-24 23:31 | +20 | HYPE | UP | 0.71 | open |  |
| 10-24 23:31 | +15 | HYPE | UP | 0.71 | open |  |
| 10-24 23:31 | +10 | HYPE | UP | 0.70 | open |  |
| 10-24 23:31 | +5 | HYPE | UP | 0.70 | open |  |
| 10-24 23:31 | +10 stop | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-24 23:31 | +20 | ETH | UP | 0.71 | open |  |
| 10-24 23:31 | +15 | ETH | UP | 0.71 | 0.90 | 1.72 |
| 10-24 23:31 | +10 | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-24 23:31 | +5 | ETH | UP | 0.71 | 0.78 | 0.42 |
| 10-24 23:31 | +10 stop | NEAR | DOWN | 0.45 | 0.30 | -1.83 |
| 10-24 23:31 | +20 | NEAR | DOWN | 0.45 | open |  |
| 10-24 23:31 | +15 | NEAR | DOWN | 0.45 | open |  |
| 10-24 23:31 | +10 | NEAR | DOWN | 0.45 | open |  |
| 10-24 23:31 | +5 | NEAR | DOWN | 0.45 | 0.53 | 0.44 |
| 10-24 23:27 | +10 stop | XRP | DOWN | 0.35 | 0.62 | 2.37 |
| 10-24 23:26 | +15 | BTC | DOWN | 0.67 | yes | -6.86 |
| 10-24 23:26 | +10 stop | BTC | DOWN | 0.68 | 0.48 | -2.34 |
| 10-24 23:25 | +10 | BTC | DOWN | 0.65 | yes | -6.66 |
| 10-24 23:25 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-24 23:25 | +10 stop | SOL | UP | 0.63 | 0.78 | 1.20 |
| 10-24 23:25 | +20 | SOL | UP | 0.62 | 0.95 | 3.10 |
| 10-24 23:25 | +15 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-24 23:25 | +10 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-24 23:25 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 10-24 23:25 | +10 stop | DOGE | UP | 0.66 | 0.50 | -1.94 |
| 10-24 23:25 | +20 | DOGE | UP | 0.66 | 0.89 | 2.07 |
| 10-24 23:25 | +15 | DOGE | UP | 0.66 | 0.82 | 1.33 |
| 10-24 23:25 | +10 | DOGE | UP | 0.66 | 0.82 | 1.33 |
| 10-24 23:25 | +5 | DOGE | UP | 0.66 | 0.82 | 1.33 |
| 10-24 23:25 | +10 stop | XRP | UP | 0.70 | 0.48 | -2.57 |
| 10-24 23:25 | +5 | XRP | UP | 0.71 | 0.80 | 0.63 |
| 10-24 23:25 | +10 stop | BTC | DOWN | 0.51 | 0.63 | 0.85 |
| 10-24 23:25 | +20 | BTC | DOWN | 0.50 | 0.70 | 1.67 |
| 10-24 23:25 | +15 | BTC | DOWN | 0.50 | 0.67 | 1.36 |
| 10-24 23:25 | +10 | BTC | DOWN | 0.50 | 0.60 | 0.65 |
| 10-24 23:25 | +5 | BTC | DOWN | 0.50 | 0.60 | 0.65 |
| 10-24 23:25 | +10 stop | NEAR | DOWN | 0.48 | 0.64 | 1.25 |
| 10-24 23:25 | +20 | NEAR | DOWN | 0.48 | 0.68 | 1.66 |
