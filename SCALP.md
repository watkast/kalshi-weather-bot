# Range-Scalp Bot

*Updated Tue Nov 24 22:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71209 | 62155 | 9054 (155) | 2 | $-18982.82 | -4.2% |
| **+10¢** | 53110 | 42533 | 10577 (201) | 4 | $-17601.46 | -5.3% |
| **+15¢** | 44485 | 33098 | 11387 (258) | 4 | $-15641.09 | -5.6% |
| **+20¢** | 39609 | 27620 | 11989 (324) | 4 | $-14018.85 | -5.6% |
| **+10¢ (15¢ stop)** | 86699 | 86498 | 201 (121) | 0 | $-31873.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 22:56 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-24 22:56 | +5 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-24 22:56 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-24 22:55 | +10 stop | ETH | UP | 0.55 | 0.37 | -2.15 |
| 11-24 22:55 | +5 | ETH | UP | 0.55 | 0.61 | 0.25 |
| 11-24 22:54 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-24 22:54 | +20 | NEAR | DOWN | 0.65 | 0.90 | 2.28 |
| 11-24 22:54 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-24 22:54 | +10 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-24 22:54 | +5 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-24 22:54 | +10 stop | BNB | DOWN | 0.70 | 0.93 | 2.06 |
| 11-24 22:54 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-24 22:53 | +10 stop | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 11-24 22:50 | +10 stop | SOL | DOWN | 0.60 | 0.32 | -3.13 |
| 11-24 22:50 | +10 stop | ZEC | UP | 0.68 | 0.50 | -2.14 |
| 11-24 22:50 | +20 | ZEC | UP | 0.68 | 0.91 | 2.05 |
| 11-24 22:50 | +15 | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 11-24 22:50 | +10 | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 11-24 22:50 | +5 | ZEC | UP | 0.68 | 0.76 | 0.51 |
| 11-24 22:50 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 11-24 22:49 | +10 stop | SOL | UP | 0.61 | 0.44 | -2.07 |
| 11-24 22:48 | +10 stop | NEAR | UP | 0.63 | 0.42 | -2.45 |
| 11-24 22:48 | +10 stop | BNB | UP | 0.58 | 0.30 | -3.13 |
| 11-24 22:48 | +20 | BNB | UP | 0.58 | open |  |
| 11-24 22:48 | +15 | BNB | UP | 0.58 | open |  |
| 11-24 22:48 | +10 | BNB | UP | 0.58 | open |  |
| 11-24 22:48 | +5 | BNB | UP | 0.58 | open |  |
| 11-24 22:48 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-24 22:48 | +20 | XRP | UP | 0.68 | 0.92 | 2.22 |
| 11-24 22:48 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-24 22:48 | +10 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-24 22:48 | +5 | XRP | UP | 0.68 | 0.74 | 0.30 |
| 11-24 22:47 | +10 stop | ETH | UP | 0.68 | 0.50 | -2.14 |
| 11-24 22:47 | +20 | ETH | UP | 0.70 | open |  |
| 11-24 22:47 | +15 | ETH | UP | 0.70 | open |  |
| 11-24 22:47 | +10 | ETH | UP | 0.70 | open |  |
| 11-24 22:47 | +5 | ETH | UP | 0.70 | 0.78 | 0.52 |
| 11-24 22:47 | +10 stop | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 11-24 22:47 | +20 | DOGE | DOWN | 0.60 | 0.80 | 1.71 |
| 11-24 22:47 | +15 | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
