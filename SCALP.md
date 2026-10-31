# Range-Scalp Bot

*Updated Sat Oct 31 14:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42325 | 36917 | 5408 (59) | 4 | $-11914.25 | -4.5% |
| **+10¢** | 31559 | 25298 | 6261 (81) | 4 | $-10710.90 | -5.4% |
| **+15¢** | 26392 | 19642 | 6750 (109) | 6 | $-9803.81 | -5.9% |
| **+20¢** | 23437 | 16365 | 7072 (141) | 7 | $-8661.43 | -5.9% |
| **+10¢ (15¢ stop)** | 51614 | 51535 | 79 (44) | 3 | $-19494.97 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 14:17 | +10 stop | DOGE | DOWN | 0.51 | 0.67 | 1.26 |
| 10-31 14:17 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-31 14:16 | +10 stop | NEAR | UP | 0.62 | open |  |
| 10-31 14:16 | +20 | NEAR | UP | 0.62 | open |  |
| 10-31 14:16 | +15 | NEAR | UP | 0.62 | open |  |
| 10-31 14:16 | +10 | NEAR | UP | 0.62 | open |  |
| 10-31 14:16 | +5 | NEAR | UP | 0.62 | 0.68 | 0.27 |
| 10-31 14:16 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 10-31 14:16 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-31 14:16 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-31 14:16 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-31 14:16 | +10 stop | BNB | UP | 0.48 | 0.58 | 0.64 |
| 10-31 14:16 | +10 | BNB | UP | 0.48 | 0.58 | 0.64 |
| 10-31 14:16 | +5 | BNB | UP | 0.48 | 0.53 | 0.14 |
| 10-31 14:16 | +5 | ZEC | UP | 0.53 | open |  |
| 10-31 14:16 | +10 stop | BNB | UP | 0.56 | 0.67 | 0.76 |
| 10-31 14:16 | +20 | BNB | UP | 0.56 | open |  |
| 10-31 14:16 | +15 | BNB | UP | 0.56 | open |  |
| 10-31 14:16 | +10 | BNB | UP | 0.56 | 0.67 | 0.76 |
| 10-31 14:16 | +5 | BNB | UP | 0.59 | 0.67 | 0.47 |
| 10-31 14:16 | +10 stop | ETH | UP | 0.40 | 0.61 | 1.76 |
| 10-31 14:16 | +20 | ETH | UP | 0.44 | open |  |
| 10-31 14:16 | +15 | ETH | UP | 0.44 | 0.61 | 1.35 |
| 10-31 14:16 | +10 | ETH | UP | 0.44 | 0.61 | 1.35 |
| 10-31 14:16 | +5 | ETH | UP | 0.44 | 0.61 | 1.35 |
| 10-31 14:16 | +10 stop | DOGE | UP | 0.58 | 0.42 | -1.96 |
| 10-31 14:16 | +20 | DOGE | UP | 0.58 | open |  |
| 10-31 14:16 | +15 | DOGE | UP | 0.58 | open |  |
| 10-31 14:16 | +10 | DOGE | UP | 0.58 | open |  |
| 10-31 14:16 | +5 | DOGE | UP | 0.58 | open |  |
| 10-31 14:16 | +10 stop | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-31 14:16 | +20 | HYPE | UP | 0.67 | open |  |
| 10-31 14:16 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-31 14:16 | +10 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-31 14:16 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 10-31 14:15 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 14:15 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-31 14:15 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-31 14:15 | +10 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 14:15 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
