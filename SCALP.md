# Range-Scalp Bot

*Updated Sun Nov 01 02:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43054 | 37535 | 5519 (62) | 6 | $-12186.37 | -4.5% |
| **+10¢** | 32102 | 25723 | 6379 (84) | 9 | $-10928.09 | -5.4% |
| **+15¢** | 26852 | 19974 | 6878 (112) | 9 | $-10024.02 | -5.9% |
| **+20¢** | 23850 | 16646 | 7204 (145) | 9 | $-8845.26 | -5.9% |
| **+10¢ (15¢ stop)** | 52511 | 52428 | 83 (48) | 0 | $-19885.85 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 02:12 | +10 stop | BTC | UP | 0.62 | 0.81 | 1.62 |
| 11-01 02:12 | +10 stop | DOGE | DOWN | 0.35 | 0.56 | 1.78 |
| 11-01 02:12 | +5 | DOGE | DOWN | 0.41 | 0.56 | 1.15 |
| 11-01 02:11 | +10 stop | BTC | DOWN | 0.65 | 0.38 | -3.03 |
| 11-01 02:11 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-01 02:11 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-01 02:11 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-01 02:11 | +5 | DOGE | UP | 0.54 | 0.59 | 0.15 |
| 11-01 02:10 | +10 stop | DOGE | UP | 0.65 | 0.42 | -2.64 |
| 11-01 02:10 | +20 | DOGE | UP | 0.65 | open |  |
| 11-01 02:10 | +15 | DOGE | UP | 0.67 | open |  |
| 11-01 02:10 | +10 | DOGE | UP | 0.60 | open |  |
| 11-01 02:10 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 11-01 02:09 | +10 stop | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-01 02:09 | +10 stop | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-01 02:09 | +5 | ETH | DOWN | 0.58 | 0.65 | 0.36 |
| 11-01 02:09 | +10 stop | SOL | DOWN | 0.61 | 0.86 | 2.24 |
| 11-01 02:09 | +10 stop | HYPE | DOWN | 0.45 | 0.56 | 0.74 |
| 11-01 02:09 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 11-01 02:09 | +20 | BTC | UP | 0.65 | open |  |
| 11-01 02:09 | +15 | BTC | UP | 0.65 | 0.83 | 1.54 |
| 11-01 02:09 | +10 | BTC | UP | 0.65 | 0.79 | 1.12 |
| 11-01 02:09 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 11-01 02:07 | +10 stop | NEAR | UP | 0.66 | 0.50 | -1.94 |
| 11-01 02:07 | +20 | NEAR | UP | 0.66 | open |  |
| 11-01 02:07 | +15 | NEAR | UP | 0.66 | open |  |
| 11-01 02:07 | +10 | NEAR | UP | 0.66 | open |  |
| 11-01 02:07 | +5 | NEAR | UP | 0.66 | open |  |
| 11-01 02:07 | +10 stop | SOL | UP | 0.71 | 0.56 | -1.83 |
| 11-01 02:07 | +20 | SOL | UP | 0.71 | open |  |
| 11-01 02:07 | +15 | SOL | UP | 0.71 | open |  |
| 11-01 02:07 | +10 | SOL | UP | 0.71 | open |  |
| 11-01 02:07 | +5 | SOL | UP | 0.71 | open |  |
| 11-01 02:07 | +10 stop | ZEC | DOWN | 0.67 | 0.48 | -2.24 |
| 11-01 02:07 | +5 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-01 02:07 | +5 | HYPE | UP | 0.65 | open |  |
| 11-01 02:07 | +10 stop | ETH | UP | 0.50 | 0.34 | -1.94 |
| 11-01 02:07 | +20 | ETH | UP | 0.50 | open |  |
| 11-01 02:07 | +15 | ETH | UP | 0.50 | open |  |
| 11-01 02:07 | +10 | ETH | UP | 0.50 | open |  |
