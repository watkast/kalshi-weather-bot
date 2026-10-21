# Range-Scalp Bot

*Updated Wed Oct 21 11:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27100 | 23599 | 3501 (39) | 4 | $-7873.69 | -4.6% |
| **+10¢** | 20383 | 16338 | 4045 (55) | 4 | $-6957.56 | -5.4% |
| **+15¢** | 17066 | 12711 | 4355 (78) | 4 | $-6235.66 | -5.8% |
| **+20¢** | 15111 | 10547 | 4564 (98) | 4 | $-5586.65 | -5.9% |
| **+10¢ (15¢ stop)** | 33242 | 33183 | 59 (32) | 4 | $-12289.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 11:03 | +10 stop | XRP | DOWN | 0.57 | open |  |
| 10-21 11:03 | +5 | XRP | DOWN | 0.59 | open |  |
| 10-21 11:03 | +5 | DOGE | UP | 0.70 | open |  |
| 10-21 11:03 | +10 stop | NEAR | UP | 0.66 | open |  |
| 10-21 11:03 | +15 | NEAR | UP | 0.66 | open |  |
| 10-21 11:03 | +10 | NEAR | UP | 0.66 | open |  |
| 10-21 11:03 | +10 stop | DOGE | UP | 0.71 | open |  |
| 10-21 11:03 | +20 | DOGE | UP | 0.71 | open |  |
| 10-21 11:03 | +15 | DOGE | UP | 0.71 | open |  |
| 10-21 11:03 | +10 | DOGE | UP | 0.71 | open |  |
| 10-21 11:03 | +5 | NEAR | UP | 0.65 | open |  |
| 10-21 11:02 | +10 stop | ZEC | UP | 0.61 | 0.81 | 1.72 |
| 10-21 11:02 | +20 | ZEC | UP | 0.60 | 0.81 | 1.82 |
| 10-21 11:02 | +15 | ZEC | UP | 0.60 | 0.81 | 1.82 |
| 10-21 11:02 | +10 | ZEC | UP | 0.61 | 0.81 | 1.72 |
| 10-21 11:02 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 10-21 11:02 | +10 stop | NEAR | UP | 0.48 | 0.64 | 1.25 |
| 10-21 11:02 | +20 | NEAR | UP | 0.47 | open |  |
| 10-21 11:02 | +15 | NEAR | UP | 0.47 | 0.64 | 1.35 |
| 10-21 11:02 | +10 | NEAR | UP | 0.47 | 0.64 | 1.35 |
| 10-21 11:02 | +5 | NEAR | UP | 0.47 | 0.56 | 0.54 |
| 10-21 11:01 | +10 stop | XRP | UP | 0.61 | 0.40 | -2.44 |
| 10-21 11:01 | +20 | XRP | UP | 0.61 | open |  |
| 10-21 11:01 | +15 | XRP | UP | 0.59 | open |  |
| 10-21 11:01 | +10 | XRP | UP | 0.59 | open |  |
| 10-21 11:01 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 10-21 11:01 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-21 11:01 | +20 | HYPE | UP | 0.64 | open |  |
| 10-21 11:01 | +15 | HYPE | UP | 0.64 | open |  |
| 10-21 11:01 | +10 | HYPE | UP | 0.64 | open |  |
| 10-21 11:01 | +5 | HYPE | UP | 0.64 | open |  |
| 10-21 11:01 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-21 11:01 | +20 | BNB | UP | 0.63 | 0.86 | 2.04 |
| 10-21 11:01 | +15 | BNB | UP | 0.63 | 0.78 | 1.20 |
| 10-21 11:01 | +10 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-21 11:01 | +5 | BNB | UP | 0.63 | 0.71 | 0.48 |
| 10-21 10:57 | +10 stop | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-21 10:57 | +5 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-21 10:56 | +10 stop | SOL | UP | 0.68 | 0.46 | -2.58 |
| 10-21 10:56 | +5 | HYPE | UP | 0.60 | 0.94 | 3.14 |
