# Range-Scalp Bot

*Updated Thu Oct 15 17:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17868 | 15510 | 2358 (28) | 3 | $-5484.76 | -4.9% |
| **+10¢** | 13493 | 10760 | 2733 (40) | 3 | $-4998.80 | -5.9% |
| **+15¢** | 11317 | 8378 | 2939 (59) | 2 | $-4504.84 | -6.3% |
| **+20¢** | 10060 | 6985 | 3075 (77) | 2 | $-3930.20 | -6.2% |
| **+10¢ (15¢ stop)** | 22008 | 21958 | 50 (29) | 0 | $-8523.50 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 17:12 | +10 stop | DOGE | UP | 0.65 | 0.84 | 1.64 |
| 10-15 17:10 | +5 | DOGE | DOWN | 0.61 | open |  |
| 10-15 17:08 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.90 |
| 10-15 17:08 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-15 17:08 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-15 17:08 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.23 |
| 10-15 17:08 | +10 stop | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-15 17:08 | +5 | SOL | UP | 0.69 | 0.85 | 1.36 |
| 10-15 17:08 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 10-15 17:08 | +10 stop | XRP | DOWN | 0.51 | 0.25 | -2.92 |
| 10-15 17:07 | +5 | SOL | UP | 0.55 | 0.60 | 0.15 |
| 10-15 17:07 | +10 stop | SOL | UP | 0.55 | 0.68 | 0.96 |
| 10-15 17:07 | +20 | SOL | UP | 0.55 | 0.85 | 2.73 |
| 10-15 17:07 | +15 | SOL | UP | 0.55 | 0.85 | 2.73 |
| 10-15 17:07 | +5 | SOL | UP | 0.55 | 0.62 | 0.35 |
| 10-15 17:07 | +10 stop | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-15 17:07 | +20 | ETH | UP | 0.69 | 0.93 | 2.20 |
| 10-15 17:07 | +15 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-15 17:07 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 10-15 17:06 | +5 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 10-15 17:06 | +10 | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-15 17:06 | +15 | BNB | UP | 0.65 | 0.82 | 1.39 |
| 10-15 17:06 | +5 | BNB | UP | 0.67 | 0.73 | 0.26 |
| 10-15 17:06 | +15 | XRP | UP | 0.65 | 0.86 | 1.85 |
| 10-15 17:06 | +10 | XRP | UP | 0.65 | 0.79 | 1.12 |
| 10-15 17:06 | +10 stop | XRP | UP | 0.65 | 0.42 | -2.64 |
| 10-15 17:06 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-15 17:06 | +20 | DOGE | DOWN | 0.61 | open |  |
| 10-15 17:06 | +15 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-15 17:06 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-15 17:06 | +5 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-15 17:05 | +10 stop | SOL | UP | 0.58 | 0.74 | 1.28 |
| 10-15 17:05 | +10 stop | HYPE | UP | 0.69 | 0.85 | 1.36 |
| 10-15 17:05 | +15 | HYPE | UP | 0.69 | 0.85 | 1.36 |
| 10-15 17:05 | +10 | HYPE | UP | 0.69 | 0.85 | 1.36 |
| 10-15 17:05 | +5 | HYPE | UP | 0.69 | 0.85 | 1.36 |
| 10-15 17:05 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.99 |
| 10-15 17:05 | +10 stop | ETH | UP | 0.60 | 0.73 | 0.99 |
| 10-15 17:05 | +5 | ETH | UP | 0.60 | 0.69 | 0.58 |
| 10-15 17:05 | +10 stop | BTC | UP | 0.62 | 0.47 | -1.85 |
