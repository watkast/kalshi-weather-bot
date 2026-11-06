# Range-Scalp Bot

*Updated Fri Nov 06 15:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49664 | 43287 | 6377 (76) | 3 | $-13980.17 | -4.5% |
| **+10¢** | 37069 | 29651 | 7418 (101) | 5 | $-12881.17 | -5.5% |
| **+15¢** | 31050 | 23058 | 7992 (130) | 5 | $-11778.75 | -6.0% |
| **+20¢** | 27604 | 19225 | 8379 (171) | 5 | $-10422.26 | -6.0% |
| **+10¢ (15¢ stop)** | 60507 | 60410 | 97 (57) | 2 | $-22372.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 15:33 | +10 stop | NEAR | DOWN | 0.63 | open |  |
| 11-06 15:33 | +20 | NEAR | DOWN | 0.63 | open |  |
| 11-06 15:33 | +15 | NEAR | DOWN | 0.63 | open |  |
| 11-06 15:33 | +10 | NEAR | DOWN | 0.63 | open |  |
| 11-06 15:33 | +5 | NEAR | DOWN | 0.63 | 0.71 | 0.48 |
| 11-06 15:33 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 11-06 15:33 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-06 15:33 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-06 15:33 | +10 | SOL | DOWN | 0.68 | open |  |
| 11-06 15:33 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-06 15:32 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-06 15:32 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-06 15:32 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-06 15:32 | +10 stop | ETH | DOWN | 0.68 | 0.44 | -2.74 |
| 11-06 15:32 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-06 15:32 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-06 15:32 | +10 | ETH | DOWN | 0.68 | open |  |
| 11-06 15:32 | +5 | ETH | DOWN | 0.68 | open |  |
| 11-06 15:32 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 11-06 15:32 | +20 | DOGE | DOWN | 0.71 | open |  |
| 11-06 15:32 | +10 stop | XRP | DOWN | 0.68 | 0.47 | -2.44 |
| 11-06 15:32 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-06 15:32 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-06 15:32 | +10 | XRP | DOWN | 0.68 | open |  |
| 11-06 15:32 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-06 15:27 | +10 stop | BTC | UP | 0.35 | 0.62 | 2.37 |
| 11-06 15:27 | +5 | BTC | UP | 0.36 | 0.62 | 2.26 |
| 11-06 15:26 | +5 | BTC | UP | 0.44 | 0.58 | 1.04 |
| 11-06 15:26 | +10 stop | XRP | DOWN | 0.63 | 0.44 | -2.25 |
| 11-06 15:26 | +5 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 11-06 15:26 | +10 stop | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 11-06 15:26 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.95 |
| 11-06 15:26 | +10 stop | BTC | UP | 0.67 | 0.37 | -3.33 |
| 11-06 15:25 | +10 stop | XRP | DOWN | 0.36 | 0.59 | 1.96 |
| 11-06 15:25 | +5 | XRP | DOWN | 0.35 | 0.59 | 2.07 |
| 11-06 15:24 | +10 stop | NEAR | DOWN | 0.70 | 0.40 | -3.32 |
| 11-06 15:24 | +10 stop | BTC | DOWN | 0.68 | 0.47 | -2.44 |
| 11-06 15:23 | +10 stop | DOGE | UP | 0.60 | 0.44 | -1.95 |
| 11-06 15:23 | +15 | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 11-06 15:23 | +10 | DOGE | UP | 0.60 | 0.73 | 0.99 |
