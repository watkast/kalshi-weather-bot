# Range-Scalp Bot

*Updated Tue Nov 17 19:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63203 | 55130 | 8073 (117) | 5 | $-17230.93 | -4.3% |
| **+10¢** | 47216 | 37770 | 9446 (159) | 6 | $-16097.90 | -5.4% |
| **+15¢** | 39583 | 29399 | 10184 (201) | 6 | $-14590.42 | -5.9% |
| **+20¢** | 35265 | 24577 | 10688 (256) | 7 | $-12843.60 | -5.8% |
| **+10¢ (15¢ stop)** | 76925 | 76769 | 156 (92) | 5 | $-28317.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 19:20 | +5 | NEAR | UP | 0.52 | open |  |
| 11-17 19:19 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-17 19:19 | +10 stop | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-17 19:19 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-17 19:19 | +10 stop | SOL | DOWN | 0.58 | open |  |
| 11-17 19:19 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-17 19:19 | +10 stop | DOGE | DOWN | 0.51 | open |  |
| 11-17 19:19 | +10 stop | BNB | DOWN | 0.63 | 0.75 | 0.87 |
| 11-17 19:19 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 11-17 19:19 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-17 19:19 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-17 19:18 | +10 stop | NEAR | UP | 0.56 | open |  |
| 11-17 19:18 | +15 | NEAR | UP | 0.56 | open |  |
| 11-17 19:18 | +10 | NEAR | UP | 0.56 | open |  |
| 11-17 19:18 | +5 | NEAR | UP | 0.56 | 0.62 | 0.25 |
| 11-17 19:18 | +5 | DOGE | UP | 0.56 | open |  |
| 11-17 19:18 | +5 | XRP | UP | 0.60 | open |  |
| 11-17 19:18 | +10 stop | SOL | UP | 0.59 | 0.39 | -2.34 |
| 11-17 19:18 | +20 | SOL | UP | 0.58 | open |  |
| 11-17 19:18 | +15 | SOL | UP | 0.58 | open |  |
| 11-17 19:18 | +10 | SOL | UP | 0.57 | open |  |
| 11-17 19:18 | +5 | DOGE | UP | 0.58 | 0.65 | 0.36 |
| 11-17 19:18 | +10 stop | XRP | UP | 0.60 | open |  |
| 11-17 19:18 | +15 | XRP | UP | 0.60 | open |  |
| 11-17 19:18 | +10 | XRP | UP | 0.59 | open |  |
| 11-17 19:18 | +5 | XRP | UP | 0.59 | 0.66 | 0.33 |
| 11-17 19:18 | +10 stop | DOGE | UP | 0.66 | 0.41 | -2.83 |
| 11-17 19:18 | +10 | DOGE | UP | 0.66 | open |  |
| 11-17 19:18 | +10 stop | HYPE | UP | 0.56 | 0.39 | -2.05 |
| 11-17 19:18 | +15 | HYPE | UP | 0.56 | open |  |
| 11-17 19:18 | +10 | HYPE | UP | 0.56 | open |  |
| 11-17 19:18 | +5 | HYPE | UP | 0.56 | open |  |
| 11-17 19:17 | +10 | ZEC | UP | 0.53 | open |  |
| 11-17 19:17 | +10 stop | ETH | UP | 0.52 | 0.37 | -1.85 |
| 11-17 19:17 | +10 stop | BTC | UP | 0.51 | 0.36 | -1.85 |
| 11-17 19:17 | +5 | DOGE | UP | 0.63 | 0.69 | 0.30 |
| 11-17 19:17 | +10 stop | BNB | UP | 0.52 | 0.35 | -2.04 |
| 11-17 19:17 | +10 stop | ZEC | UP | 0.53 | 0.33 | -2.34 |
| 11-17 19:16 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.48 |
| 11-17 19:16 | +10 stop | ETH | DOWN | 0.58 | 0.37 | -2.45 |
