# Range-Scalp Bot

*Updated Thu Oct 29 10:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39097 | 34113 | 4984 (49) | 2 | $-11012.75 | -4.5% |
| **+10¢** | 29161 | 23408 | 5753 (71) | 5 | $-9752.51 | -5.3% |
| **+15¢** | 24388 | 18208 | 6180 (98) | 6 | $-8708.43 | -5.7% |
| **+20¢** | 21635 | 15159 | 6476 (127) | 8 | $-7621.11 | -5.6% |
| **+10¢ (15¢ stop)** | 47796 | 47729 | 67 (35) | 2 | $-18141.32 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 10:03 | +5 | DOGE | DOWN | 0.61 | 0.66 | 0.17 |
| 10-29 10:03 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 10-29 10:01 | +5 | NEAR | UP | 0.56 | open |  |
| 10-29 10:01 | +10 stop | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-29 10:01 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-29 10:01 | +15 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 10-29 10:01 | +10 | ETH | DOWN | 0.60 | 0.71 | 0.76 |
| 10-29 10:01 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.35 |
| 10-29 10:01 | +10 stop | SOL | DOWN | 0.53 | 0.65 | 0.86 |
| 10-29 10:01 | +20 | SOL | DOWN | 0.53 | open |  |
| 10-29 10:01 | +15 | SOL | DOWN | 0.53 | open |  |
| 10-29 10:01 | +10 | SOL | DOWN | 0.56 | open |  |
| 10-29 10:01 | +5 | SOL | DOWN | 0.56 | 0.65 | 0.56 |
| 10-29 10:01 | +10 stop | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-29 10:01 | +10 stop | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-29 10:01 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-29 10:01 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-29 10:01 | +10 | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-29 10:01 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-29 10:01 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-29 10:01 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-29 10:01 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-29 10:01 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-29 10:01 | +5 | HYPE | DOWN | 0.61 | 0.70 | 0.61 |
| 10-29 10:01 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 10-29 10:01 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-29 10:01 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-29 10:01 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-29 10:01 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-29 10:01 | +10 stop | BTC | DOWN | 0.71 | 0.54 | -2.03 |
| 10-29 10:01 | +20 | BTC | DOWN | 0.71 | open |  |
| 10-29 10:01 | +15 | BTC | DOWN | 0.71 | open |  |
| 10-29 10:01 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-29 10:01 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 10-29 10:01 | +10 stop | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 10-29 10:01 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-29 10:01 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-29 10:01 | +10 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-29 10:01 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 10-29 10:01 | +10 stop | NEAR | UP | 0.49 | open |  |
