# Range-Scalp Bot

*Updated Fri Nov 13 09:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58045 | 50642 | 7403 (102) | 0 | $-15706.08 | -4.3% |
| **+10¢** | 43363 | 34710 | 8653 (134) | 2 | $-14670.95 | -5.4% |
| **+15¢** | 36355 | 27040 | 9315 (168) | 3 | $-13220.64 | -5.8% |
| **+20¢** | 32392 | 22613 | 9779 (219) | 3 | $-11597.60 | -5.7% |
| **+10¢ (15¢ stop)** | 70718 | 70589 | 129 (79) | 2 | $-26009.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 09:02 | +10 stop | HYPE | UP | 0.70 | open |  |
| 11-13 09:02 | +20 | HYPE | UP | 0.70 | open |  |
| 11-13 09:02 | +15 | HYPE | UP | 0.71 | open |  |
| 11-13 09:02 | +10 | HYPE | UP | 0.71 | open |  |
| 11-13 09:02 | +5 | HYPE | UP | 0.71 | 0.77 | 0.32 |
| 11-13 09:01 | +10 stop | BTC | UP | 0.70 | open |  |
| 11-13 09:01 | +20 | BTC | UP | 0.71 | open |  |
| 11-13 09:01 | +15 | BTC | UP | 0.71 | open |  |
| 11-13 09:01 | +10 | BTC | UP | 0.71 | open |  |
| 11-13 09:01 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 11-13 09:01 | +10 stop | ZEC | UP | 0.59 | 0.73 | 1.09 |
| 11-13 09:01 | +20 | ZEC | UP | 0.59 | 0.79 | 1.71 |
| 11-13 09:01 | +15 | ZEC | UP | 0.59 | 0.79 | 1.71 |
| 11-13 09:01 | +10 | ZEC | UP | 0.59 | 0.73 | 1.09 |
| 11-13 09:01 | +5 | ZEC | UP | 0.59 | 0.64 | 0.16 |
| 11-13 09:01 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 11-13 09:01 | +20 | ETH | UP | 0.67 | 0.89 | 1.97 |
| 11-13 09:01 | +15 | ETH | UP | 0.67 | 0.84 | 1.44 |
| 11-13 09:01 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 11-13 09:01 | +5 | ETH | UP | 0.67 | 0.74 | 0.40 |
| 11-13 09:01 | +10 stop | DOGE | UP | 0.57 | 0.71 | 1.07 |
| 11-13 09:01 | +10 | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-13 09:01 | +5 | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-13 09:00 | +10 stop | NEAR | UP | 0.62 | 0.86 | 2.14 |
| 11-13 09:00 | +20 | NEAR | UP | 0.62 | 0.86 | 2.14 |
| 11-13 09:00 | +15 | NEAR | UP | 0.62 | 0.86 | 2.14 |
| 11-13 09:00 | +10 | NEAR | UP | 0.62 | 0.86 | 2.14 |
| 11-13 09:00 | +5 | NEAR | UP | 0.62 | 0.68 | 0.27 |
| 11-13 09:00 | +10 stop | DOGE | DOWN | 0.48 | 0.60 | 0.80 |
| 11-13 09:00 | +20 | DOGE | DOWN | 0.48 | open |  |
| 11-13 09:00 | +15 | DOGE | DOWN | 0.48 | open |  |
| 11-13 09:00 | +10 | DOGE | DOWN | 0.48 | 0.60 | 0.80 |
| 11-13 09:00 | +5 | DOGE | DOWN | 0.48 | 0.60 | 0.80 |
| 11-13 08:58 | +10 stop | ETH | DOWN | 0.53 | 0.14 | -4.17 |
| 11-13 08:58 | +20 | ETH | DOWN | 0.53 | yes | -5.48 |
| 11-13 08:58 | +15 | ETH | DOWN | 0.53 | yes | -5.48 |
| 11-13 08:58 | +10 | ETH | DOWN | 0.54 | yes | -5.58 |
| 11-13 08:58 | +5 | ETH | DOWN | 0.54 | yes | -5.58 |
| 11-13 08:58 | +10 stop | DOGE | UP | 0.62 | 0.84 | 1.89 |
| 11-13 08:58 | +20 | DOGE | UP | 0.62 | 0.84 | 1.88 |
