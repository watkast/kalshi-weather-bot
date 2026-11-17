# Range-Scalp Bot

*Updated Tue Nov 17 06:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62722 | 54714 | 8008 (117) | 1 | $-17047.88 | -4.3% |
| **+10¢** | 46836 | 37462 | 9374 (159) | 3 | $-15960.75 | -5.4% |
| **+15¢** | 39252 | 29142 | 10110 (201) | 5 | $-14519.25 | -5.9% |
| **+20¢** | 34987 | 24386 | 10601 (256) | 5 | $-12685.44 | -5.8% |
| **+10¢ (15¢ stop)** | 76314 | 76158 | 156 (92) | 0 | $-28131.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 06:31 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-17 06:31 | +20 | ZEC | DOWN | 0.64 | 0.93 | 2.63 |
| 11-17 06:31 | +15 | ZEC | DOWN | 0.64 | 0.83 | 1.63 |
| 11-17 06:31 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-17 06:31 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.38 |
| 11-17 06:31 | +10 stop | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-17 06:31 | +10 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-17 06:31 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 11-17 06:31 | +10 stop | SOL | UP | 0.46 | 0.58 | 0.84 |
| 11-17 06:31 | +20 | SOL | UP | 0.46 | open |  |
| 11-17 06:31 | +15 | SOL | UP | 0.46 | open |  |
| 11-17 06:31 | +10 | SOL | UP | 0.46 | 0.58 | 0.84 |
| 11-17 06:31 | +5 | SOL | UP | 0.46 | 0.58 | 0.84 |
| 11-17 06:31 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 06:31 | +20 | HYPE | DOWN | 0.71 | 0.96 | 2.34 |
| 11-17 06:31 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-17 06:31 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 06:31 | +5 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 06:31 | +10 stop | BTC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-17 06:31 | +20 | BTC | DOWN | 0.71 | 0.93 | 1.99 |
| 11-17 06:31 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-17 06:31 | +10 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-17 06:31 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-17 06:31 | +5 | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 11-17 06:31 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.23 |
| 11-17 06:31 | +10 stop | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 11-17 06:31 | +20 | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 11-17 06:31 | +15 | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 11-17 06:31 | +10 | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 11-17 06:31 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 11-17 06:30 | +10 stop | BNB | UP | 0.49 | 0.26 | -2.61 |
| 11-17 06:30 | +20 | BNB | UP | 0.49 | open |  |
| 11-17 06:30 | +15 | BNB | UP | 0.49 | open |  |
| 11-17 06:30 | +10 | BNB | UP | 0.49 | open |  |
| 11-17 06:30 | +5 | BNB | UP | 0.49 | 0.56 | 0.35 |
| 11-17 06:30 | +10 stop | DOGE | UP | 0.59 | 0.27 | -3.51 |
| 11-17 06:30 | +20 | DOGE | UP | 0.59 | open |  |
| 11-17 06:30 | +15 | DOGE | UP | 0.59 | open |  |
| 11-17 06:30 | +10 | DOGE | UP | 0.59 | open |  |
| 11-17 06:30 | +5 | DOGE | UP | 0.59 | open |  |
