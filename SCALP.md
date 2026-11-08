# Range-Scalp Bot

*Updated Sun Nov 08 16:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52527 | 45790 | 6737 (83) | 4 | $-14595.92 | -4.4% |
| **+10¢** | 39209 | 31361 | 7848 (108) | 6 | $-13566.01 | -5.5% |
| **+15¢** | 32849 | 24390 | 8459 (138) | 6 | $-12439.13 | -6.0% |
| **+20¢** | 29221 | 20357 | 8864 (182) | 6 | $-10933.59 | -6.0% |
| **+10¢ (15¢ stop)** | 63973 | 63867 | 106 (63) | 3 | $-23719.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 16:48 | +10 stop | HYPE | DOWN | 0.60 | open |  |
| 11-08 16:48 | +10 | HYPE | DOWN | 0.61 | open |  |
| 11-08 16:48 | +5 | HYPE | DOWN | 0.61 | open |  |
| 11-08 16:47 | +10 stop | HYPE | DOWN | 0.51 | 0.62 | 0.75 |
| 11-08 16:47 | +20 | HYPE | DOWN | 0.51 | open |  |
| 11-08 16:47 | +15 | HYPE | DOWN | 0.51 | open |  |
| 11-08 16:47 | +10 | HYPE | DOWN | 0.51 | 0.62 | 0.75 |
| 11-08 16:47 | +5 | HYPE | DOWN | 0.51 | 0.62 | 0.75 |
| 11-08 16:47 | +10 stop | SOL | UP | 0.46 | open |  |
| 11-08 16:47 | +5 | SOL | UP | 0.46 | 0.54 | 0.44 |
| 11-08 16:47 | +10 stop | BTC | UP | 0.52 | open |  |
| 11-08 16:46 | +10 stop | BNB | UP | 0.51 | 0.26 | -2.82 |
| 11-08 16:46 | +20 | BNB | UP | 0.51 | open |  |
| 11-08 16:46 | +15 | BNB | UP | 0.51 | open |  |
| 11-08 16:46 | +10 | BNB | UP | 0.51 | open |  |
| 11-08 16:46 | +5 | BNB | UP | 0.51 | open |  |
| 11-08 16:46 | +5 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-08 16:46 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-08 16:46 | +20 | NEAR | DOWN | 0.64 | 0.86 | 1.94 |
| 11-08 16:46 | +15 | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 11-08 16:46 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 16:46 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-08 16:46 | +5 | BTC | UP | 0.64 | open |  |
| 11-08 16:45 | +10 stop | SOL | UP | 0.61 | 0.40 | -2.44 |
| 11-08 16:45 | +20 | SOL | UP | 0.61 | open |  |
| 11-08 16:45 | +15 | SOL | UP | 0.61 | open |  |
| 11-08 16:45 | +10 | SOL | UP | 0.61 | open |  |
| 11-08 16:45 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 11-08 16:45 | +10 stop | BTC | UP | 0.60 | 0.42 | -2.15 |
| 11-08 16:45 | +20 | BTC | UP | 0.60 | open |  |
| 11-08 16:45 | +15 | BTC | UP | 0.60 | open |  |
| 11-08 16:45 | +10 | BTC | UP | 0.59 | open |  |
| 11-08 16:45 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-08 16:45 | +10 stop | DOGE | UP | 0.47 | 0.20 | -3.00 |
| 11-08 16:45 | +20 | DOGE | UP | 0.47 | open |  |
| 11-08 16:45 | +15 | DOGE | UP | 0.47 | open |  |
| 11-08 16:45 | +10 | DOGE | UP | 0.47 | open |  |
| 11-08 16:45 | +5 | DOGE | UP | 0.47 | 0.52 | 0.14 |
| 11-08 16:45 | +10 stop | ETH | UP | 0.60 | 0.41 | -2.24 |
| 11-08 16:45 | +20 | ETH | UP | 0.60 | open |  |
