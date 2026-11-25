# Range-Scalp Bot

*Updated Wed Nov 25 05:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71503 | 62413 | 9090 (157) | 0 | $-19024.09 | -4.2% |
| **+10¢** | 53332 | 42713 | 10619 (203) | 1 | $-17642.97 | -5.3% |
| **+15¢** | 44666 | 33234 | 11432 (260) | 1 | $-15680.15 | -5.6% |
| **+20¢** | 39767 | 27725 | 12042 (326) | 1 | $-14105.59 | -5.7% |
| **+10¢ (15¢ stop)** | 87061 | 86858 | 203 (123) | 0 | $-32009.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 05:36 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 11-25 05:36 | +5 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-25 05:36 | +5 | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 11-25 05:36 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.85 |
| 11-25 05:35 | +10 stop | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 11-25 05:35 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-25 05:35 | +10 stop | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-25 05:35 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-25 05:35 | +5 | XRP | DOWN | 0.53 | 0.70 | 1.37 |
| 11-25 05:35 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-25 05:34 | +10 stop | XRP | UP | 0.50 | 0.28 | -2.53 |
| 11-25 05:34 | +15 | XRP | UP | 0.50 | open |  |
| 11-25 05:34 | +10 | XRP | UP | 0.50 | open |  |
| 11-25 05:34 | +5 | XRP | UP | 0.50 | 0.59 | 0.55 |
| 11-25 05:34 | +10 stop | DOGE | DOWN | 0.50 | 0.60 | 0.65 |
| 11-25 05:34 | +10 stop | ZEC | DOWN | 0.66 | 0.81 | 1.26 |
| 11-25 05:34 | +20 | ZEC | DOWN | 0.66 | 0.93 | 2.50 |
| 11-25 05:34 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.26 |
| 11-25 05:34 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.26 |
| 11-25 05:34 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.22 |
| 11-25 05:33 | +10 stop | HYPE | UP | 0.62 | 0.42 | -2.35 |
| 11-25 05:33 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 11-25 05:33 | +10 stop | BNB | UP | 0.58 | 0.43 | -1.86 |
| 11-25 05:33 | +10 stop | SOL | UP | 0.47 | 0.32 | -1.84 |
| 11-25 05:32 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 11-25 05:32 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-25 05:32 | +20 | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 11-25 05:32 | +15 | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 11-25 05:32 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-25 05:32 | +5 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-25 05:31 | +10 stop | DOGE | DOWN | 0.61 | 0.46 | -1.85 |
| 11-25 05:31 | +20 | DOGE | DOWN | 0.61 | 0.82 | 1.82 |
| 11-25 05:31 | +15 | DOGE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-25 05:31 | +10 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 05:31 | +5 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 05:31 | +10 stop | XRP | UP | 0.58 | 0.72 | 1.07 |
| 11-25 05:31 | +20 | XRP | UP | 0.58 | open |  |
| 11-25 05:31 | +15 | XRP | UP | 0.58 | 0.73 | 1.18 |
| 11-25 05:31 | +10 | XRP | UP | 0.58 | 0.72 | 1.07 |
| 11-25 05:31 | +5 | XRP | UP | 0.58 | 0.65 | 0.36 |
