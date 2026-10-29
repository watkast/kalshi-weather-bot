# Range-Scalp Bot

*Updated Thu Oct 29 10:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39108 | 34124 | 4984 (49) | 1 | $-11008.11 | -4.5% |
| **+10¢** | 29167 | 23414 | 5753 (71) | 2 | $-9746.31 | -5.3% |
| **+15¢** | 24394 | 18214 | 6180 (98) | 2 | $-8699.87 | -5.7% |
| **+20¢** | 21641 | 15165 | 6476 (127) | 2 | $-7609.67 | -5.6% |
| **+10¢ (15¢ stop)** | 47811 | 47744 | 67 (35) | 0 | $-18146.50 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 10:13 | +10 stop | ZEC | UP | 0.46 | 0.28 | -2.13 |
| 10-29 10:13 | +5 | ZEC | UP | 0.46 | 0.52 | 0.24 |
| 10-29 10:12 | +10 stop | ZEC | DOWN | 0.40 | 0.68 | 2.47 |
| 10-29 10:10 | +10 stop | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-29 10:09 | +10 stop | ZEC | UP | 0.59 | 0.39 | -2.34 |
| 10-29 10:09 | +15 | ZEC | UP | 0.60 | open |  |
| 10-29 10:09 | +5 | ZEC | UP | 0.60 | 0.68 | 0.47 |
| 10-29 10:07 | +10 stop | SOL | UP | 0.53 | 0.67 | 1.06 |
| 10-29 10:07 | +10 stop | ZEC | DOWN | 0.70 | 0.45 | -2.83 |
| 10-29 10:07 | +10 | ZEC | DOWN | 0.70 | open |  |
| 10-29 10:07 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-29 10:07 | +10 stop | NEAR | DOWN | 0.57 | 0.71 | 1.07 |
| 10-29 10:06 | +10 stop | SOL | UP | 0.66 | 0.45 | -2.44 |
| 10-29 10:05 | +5 | NEAR | UP | 0.53 | open |  |
| 10-29 10:05 | +10 stop | NEAR | UP | 0.57 | 0.39 | -2.15 |
| 10-29 10:05 | +10 | NEAR | UP | 0.57 | open |  |
| 10-29 10:05 | +5 | NEAR | UP | 0.57 | 0.64 | 0.35 |
| 10-29 10:05 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-29 10:05 | +5 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-29 10:05 | +5 | HYPE | DOWN | 0.55 | 0.60 | 0.15 |
| 10-29 10:04 | +10 stop | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-29 10:04 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.35 |
| 10-29 10:04 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-29 10:04 | +15 | ETH | DOWN | 0.67 | 0.87 | 1.80 |
| 10-29 10:04 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-29 10:04 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 10-29 10:04 | +10 stop | SOL | DOWN | 0.65 | 0.34 | -3.42 |
| 10-29 10:04 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-29 10:03 | +5 | DOGE | DOWN | 0.61 | 0.66 | 0.17 |
| 10-29 10:03 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 10-29 10:01 | +5 | NEAR | UP | 0.56 | 0.63 | 0.35 |
| 10-29 10:01 | +10 stop | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-29 10:01 | +20 | ETH | DOWN | 0.60 | 0.81 | 1.82 |
| 10-29 10:01 | +15 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 10-29 10:01 | +10 | ETH | DOWN | 0.60 | 0.71 | 0.76 |
| 10-29 10:01 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.35 |
| 10-29 10:01 | +10 stop | SOL | DOWN | 0.53 | 0.65 | 0.86 |
| 10-29 10:01 | +20 | SOL | DOWN | 0.53 | 0.74 | 1.78 |
| 10-29 10:01 | +15 | SOL | DOWN | 0.53 | 0.74 | 1.78 |
| 10-29 10:01 | +10 | SOL | DOWN | 0.56 | 0.74 | 1.48 |
