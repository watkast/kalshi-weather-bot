# Range-Scalp Bot

*Updated Thu Nov 19 17:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65203 | 56919 | 8284 (124) | 0 | $-17442.55 | -4.2% |
| **+10¢** | 48694 | 39001 | 9693 (165) | 2 | $-16245.01 | -5.3% |
| **+15¢** | 40830 | 30374 | 10456 (211) | 2 | $-14633.86 | -5.7% |
| **+20¢** | 36361 | 25376 | 10985 (266) | 2 | $-12958.60 | -5.7% |
| **+10¢ (15¢ stop)** | 79382 | 79218 | 164 (98) | 0 | $-29235.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 16:50 | +10 stop | NEAR | UP | 0.53 | 0.64 | 0.75 |
| 11-19 16:50 | +10 | NEAR | UP | 0.55 | open |  |
| 11-19 16:50 | +5 | NEAR | UP | 0.56 | 0.64 | 0.44 |
| 11-19 16:50 | +10 stop | HYPE | UP | 0.52 | 0.31 | -2.43 |
| 11-19 16:50 | +20 | HYPE | UP | 0.52 | open |  |
| 11-19 16:50 | +15 | HYPE | UP | 0.51 | open |  |
| 11-19 16:50 | +10 | HYPE | UP | 0.51 | open |  |
| 11-19 16:50 | +5 | HYPE | UP | 0.50 | 0.55 | 0.14 |
| 11-19 16:50 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.85 |
| 11-19 16:50 | +10 stop | ZEC | DOWN | 0.66 | 0.81 | 1.25 |
| 11-19 16:50 | +10 stop | SOL | DOWN | 0.61 | 0.83 | 1.93 |
| 11-19 16:50 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-19 16:49 | +10 stop | SOL | UP | 0.53 | 0.65 | 0.86 |
| 11-19 16:49 | +10 stop | ZEC | UP | 0.67 | 0.40 | -3.03 |
| 11-19 16:49 | +10 stop | ETH | UP | 0.64 | 0.46 | -2.15 |
| 11-19 16:48 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-19 16:48 | +20 | NEAR | UP | 0.70 | open |  |
| 11-19 16:48 | +15 | NEAR | UP | 0.70 | open |  |
| 11-19 16:48 | +10 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-19 16:48 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-19 16:48 | +10 stop | BTC | DOWN | 0.60 | 0.41 | -2.24 |
| 11-19 16:47 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-19 16:47 | +10 stop | BNB | UP | 0.55 | 0.69 | 1.07 |
| 11-19 16:47 | +10 stop | DOGE | UP | 0.59 | 0.73 | 1.05 |
| 11-19 16:47 | +10 | DOGE | UP | 0.58 | 0.73 | 1.18 |
| 11-19 16:47 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 11-19 16:46 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 11-19 16:46 | +20 | ETH | DOWN | 0.60 | 0.88 | 2.55 |
| 11-19 16:46 | +15 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 11-19 16:46 | +10 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 11-19 16:46 | +5 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 11-19 16:46 | +10 stop | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-19 16:46 | +20 | DOGE | DOWN | 0.53 | 0.80 | 2.40 |
| 11-19 16:46 | +15 | DOGE | DOWN | 0.53 | 0.80 | 2.40 |
| 11-19 16:46 | +10 | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-19 16:46 | +5 | DOGE | DOWN | 0.54 | 0.63 | 0.55 |
| 11-19 16:46 | +10 stop | XRP | DOWN | 0.54 | 0.36 | -2.14 |
| 11-19 16:46 | +20 | XRP | DOWN | 0.54 | 0.81 | 2.42 |
| 11-19 16:46 | +15 | XRP | DOWN | 0.54 | 0.81 | 2.42 |
| 11-19 16:46 | +10 | XRP | DOWN | 0.54 | 0.68 | 1.07 |
