# Range-Scalp Bot

*Updated Mon Oct 19 16:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24229 | 21073 | 3156 (31) | 4 | $-7197.53 | -4.7% |
| **+10¢** | 18214 | 14572 | 3642 (46) | 7 | $-6433.30 | -5.6% |
| **+15¢** | 15260 | 11338 | 3922 (69) | 7 | $-5816.76 | -6.1% |
| **+20¢** | 13505 | 9399 | 4106 (87) | 7 | $-5220.12 | -6.2% |
| **+10¢ (15¢ stop)** | 29826 | 29774 | 52 (30) | 0 | $-11327.78 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 16:09 | +10 stop | BTC | UP | 0.53 | 0.65 | 0.86 |
| 10-19 16:08 | +10 | BNB | UP | 0.69 | 0.81 | 0.90 |
| 10-19 16:08 | +5 | DOGE | UP | 0.62 | 0.79 | 1.41 |
| 10-19 16:08 | +10 stop | BNB | UP | 0.69 | 0.81 | 0.94 |
| 10-19 16:08 | +5 | BNB | UP | 0.69 | 0.77 | 0.52 |
| 10-19 16:08 | +10 stop | ETH | UP | 0.70 | 0.82 | 0.94 |
| 10-19 16:08 | +5 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-19 16:08 | +5 | BTC | DOWN | 0.66 | open |  |
| 10-19 16:07 | +5 | DOGE | DOWN | 0.48 | 0.58 | 0.64 |
| 10-19 16:07 | +10 stop | XRP | DOWN | 0.55 | 0.40 | -1.85 |
| 10-19 16:07 | +10 | XRP | DOWN | 0.55 | open |  |
| 10-19 16:07 | +5 | XRP | DOWN | 0.55 | 0.61 | 0.25 |
| 10-19 16:07 | +10 stop | HYPE | DOWN | 0.54 | 0.35 | -2.24 |
| 10-19 16:07 | +10 stop | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 10-19 16:07 | +10 stop | SOL | UP | 0.62 | 0.77 | 1.20 |
| 10-19 16:07 | +5 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 10-19 16:07 | +10 stop | ZEC | UP | 0.65 | 0.85 | 1.78 |
| 10-19 16:07 | +20 | ZEC | UP | 0.65 | 0.85 | 1.78 |
| 10-19 16:07 | +15 | ZEC | UP | 0.65 | 0.85 | 1.78 |
| 10-19 16:07 | +10 | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-19 16:07 | +5 | BNB | UP | 0.56 | 0.64 | 0.45 |
| 10-19 16:07 | +10 stop | HYPE | UP | 0.42 | 0.54 | 0.84 |
| 10-19 16:07 | +10 stop | ETH | UP | 0.50 | 0.61 | 0.75 |
| 10-19 16:07 | +5 | ETH | UP | 0.52 | 0.57 | 0.14 |
| 10-19 16:06 | +10 stop | XRP | DOWN | 0.51 | 0.66 | 1.17 |
| 10-19 16:06 | +10 | XRP | DOWN | 0.51 | 0.66 | 1.17 |
| 10-19 16:06 | +5 | XRP | DOWN | 0.51 | 0.66 | 1.16 |
| 10-19 16:06 | +10 stop | BNB | UP | 0.64 | 0.48 | -1.95 |
| 10-19 16:06 | +5 | ETH | DOWN | 0.53 | 0.58 | 0.14 |
| 10-19 16:06 | +10 stop | HYPE | DOWN | 0.63 | 0.43 | -2.35 |
| 10-19 16:06 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-19 16:06 | +10 stop | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-19 16:06 | +5 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-19 16:05 | +10 | ZEC | UP | 0.52 | 0.70 | 1.47 |
| 10-19 16:05 | +10 stop | BNB | UP | 0.46 | 0.57 | 0.74 |
| 10-19 16:05 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-19 16:05 | +10 stop | NEAR | UP | 0.60 | 0.74 | 1.09 |
| 10-19 16:05 | +10 stop | HYPE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-19 16:05 | +20 | HYPE | DOWN | 0.59 | open |  |
| 10-19 16:05 | +15 | HYPE | DOWN | 0.59 | open |  |
