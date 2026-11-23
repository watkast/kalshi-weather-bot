# Range-Scalp Bot

*Updated Mon Nov 23 05:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69645 | 60773 | 8872 (146) | 8 | $-18725.56 | -4.3% |
| **+10¢** | 51963 | 41598 | 10365 (189) | 8 | $-17418.91 | -5.3% |
| **+15¢** | 43543 | 32376 | 11167 (244) | 8 | $-15571.44 | -5.7% |
| **+20¢** | 38778 | 27034 | 11744 (308) | 8 | $-13887.37 | -5.7% |
| **+10¢ (15¢ stop)** | 84809 | 84619 | 190 (118) | 0 | $-31205.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 05:08 | +10 stop | NEAR | UP | 0.65 | 0.80 | 1.25 |
| 11-23 05:08 | +20 | NEAR | UP | 0.61 | 0.86 | 2.24 |
| 11-23 05:08 | +15 | NEAR | UP | 0.61 | 0.80 | 1.61 |
| 11-23 05:08 | +10 | NEAR | UP | 0.61 | 0.80 | 1.61 |
| 11-23 05:08 | +5 | NEAR | UP | 0.61 | 0.67 | 0.22 |
| 11-23 05:07 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-23 05:06 | +10 stop | BTC | UP | 0.57 | 0.28 | -3.23 |
| 11-23 05:06 | +10 stop | SOL | UP | 0.62 | 0.40 | -2.54 |
| 11-23 05:06 | +10 stop | ETH | UP | 0.61 | 0.31 | -3.32 |
| 11-23 05:06 | +10 stop | HYPE | DOWN | 0.58 | 0.76 | 1.49 |
| 11-23 05:06 | +10 stop | DOGE | UP | 0.64 | 0.32 | -3.53 |
| 11-23 05:06 | +10 stop | ZEC | DOWN | 0.50 | 0.72 | 1.87 |
| 11-23 05:05 | +10 stop | XRP | DOWN | 0.57 | 0.69 | 0.87 |
| 11-23 05:05 | +5 | DOGE | UP | 0.71 | open |  |
| 11-23 05:05 | +5 | HYPE | UP | 0.64 | open |  |
| 11-23 05:04 | +10 stop | BTC | UP | 0.63 | 0.42 | -2.45 |
| 11-23 05:04 | +5 | ETH | UP | 0.67 | open |  |
| 11-23 05:04 | +10 stop | ZEC | UP | 0.64 | 0.37 | -3.04 |
| 11-23 05:04 | +10 | ZEC | UP | 0.64 | open |  |
| 11-23 05:04 | +5 | ZEC | UP | 0.64 | open |  |
| 11-23 05:02 | +5 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 11-23 05:02 | +5 | BNB | UP | 0.63 | open |  |
| 11-23 05:01 | +10 stop | BNB | UP | 0.56 | 0.28 | -3.13 |
| 11-23 05:01 | +20 | BNB | UP | 0.56 | open |  |
| 11-23 05:01 | +15 | BNB | UP | 0.56 | open |  |
| 11-23 05:01 | +10 | BNB | UP | 0.56 | open |  |
| 11-23 05:01 | +5 | BNB | UP | 0.56 | 0.64 | 0.45 |
| 11-23 05:01 | +10 stop | BTC | UP | 0.70 | 0.54 | -1.93 |
| 11-23 05:01 | +20 | BTC | UP | 0.70 | open |  |
| 11-23 05:01 | +15 | BTC | UP | 0.70 | open |  |
| 11-23 05:01 | +10 | BTC | UP | 0.70 | open |  |
| 11-23 05:01 | +5 | BTC | UP | 0.70 | open |  |
| 11-23 05:01 | +10 stop | SOL | UP | 0.69 | 0.45 | -2.73 |
| 11-23 05:01 | +20 | SOL | UP | 0.69 | open |  |
| 11-23 05:01 | +15 | SOL | UP | 0.69 | open |  |
| 11-23 05:01 | +10 | SOL | UP | 0.69 | open |  |
| 11-23 05:01 | +5 | SOL | UP | 0.69 | open |  |
| 11-23 05:01 | +10 stop | ETH | UP | 0.70 | 0.49 | -2.43 |
| 11-23 05:01 | +20 | ETH | UP | 0.70 | open |  |
| 11-23 05:01 | +15 | ETH | UP | 0.70 | open |  |
