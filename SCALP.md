# Range-Scalp Bot

*Updated Thu Oct 15 01:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16861 | 14627 | 2234 (28) | 1 | $-5209.88 | -4.9% |
| **+10¢** | 12751 | 10160 | 2591 (40) | 1 | $-4754.22 | -5.9% |
| **+15¢** | 10714 | 7927 | 2787 (59) | 1 | $-4280.10 | -6.4% |
| **+20¢** | 9521 | 6600 | 2921 (76) | 1 | $-3787.99 | -6.3% |
| **+10¢ (15¢ stop)** | 20776 | 20726 | 50 (29) | 0 | $-8057.53 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 01:27 | +10 stop | ZEC | DOWN | 0.63 | 0.86 | 2.02 |
| 10-15 01:22 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-15 01:22 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-15 01:22 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-15 01:22 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-15 01:21 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.74 |
| 10-15 01:20 | +10 stop | SOL | UP | 0.62 | 0.47 | -1.85 |
| 10-15 01:20 | +10 stop | XRP | UP | 0.64 | 0.39 | -2.84 |
| 10-15 01:20 | +10 stop | ETH | UP | 0.63 | 0.35 | -3.13 |
| 10-15 01:20 | +10 stop | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 10-15 01:20 | +5 | ZEC | UP | 0.63 | open |  |
| 10-15 01:20 | +10 stop | BNB | DOWN | 0.53 | 0.69 | 1.27 |
| 10-15 01:20 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-15 01:20 | +10 stop | ZEC | UP | 0.56 | 0.35 | -2.44 |
| 10-15 01:20 | +20 | ZEC | UP | 0.55 | open |  |
| 10-15 01:20 | +15 | ZEC | UP | 0.55 | open |  |
| 10-15 01:20 | +10 | ZEC | UP | 0.55 | open |  |
| 10-15 01:20 | +5 | ZEC | UP | 0.55 | 0.60 | 0.15 |
| 10-15 01:19 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 10-15 01:19 | +10 stop | ETH | UP | 0.71 | 0.48 | -2.63 |
| 10-15 01:19 | +10 stop | DOGE | UP | 0.59 | 0.38 | -2.44 |
| 10-15 01:18 | +10 stop | SOL | UP | 0.63 | 0.45 | -2.15 |
| 10-15 01:18 | +10 stop | HYPE | UP | 0.60 | 0.42 | -2.15 |
| 10-15 01:18 | +10 stop | BTC | UP | 0.64 | 0.47 | -2.05 |
| 10-15 01:18 | +10 stop | BNB | UP | 0.62 | 0.46 | -1.95 |
| 10-15 01:16 | +10 stop | NEAR | DOWN | 0.66 | 0.46 | -2.34 |
| 10-15 01:16 | +20 | NEAR | DOWN | 0.66 | 0.86 | 1.75 |
| 10-15 01:16 | +15 | NEAR | DOWN | 0.66 | 0.84 | 1.54 |
| 10-15 01:16 | +10 | NEAR | DOWN | 0.66 | 0.84 | 1.54 |
| 10-15 01:16 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-15 01:16 | +10 stop | BNB | DOWN | 0.69 | 0.45 | -2.72 |
| 10-15 01:16 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.79 |
| 10-15 01:16 | +15 | BNB | DOWN | 0.69 | 0.84 | 1.26 |
| 10-15 01:16 | +10 | BNB | DOWN | 0.69 | 0.84 | 1.26 |
| 10-15 01:16 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.22 |
| 10-15 01:16 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-15 01:16 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-15 01:16 | +15 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-15 01:16 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 01:16 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
