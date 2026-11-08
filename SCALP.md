# Range-Scalp Bot

*Updated Sun Nov 08 17:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52545 | 45805 | 6740 (83) | 0 | $-14606.32 | -4.4% |
| **+10¢** | 39224 | 31371 | 7853 (108) | 1 | $-13585.32 | -5.5% |
| **+15¢** | 32863 | 24399 | 8464 (138) | 1 | $-12454.52 | -6.0% |
| **+20¢** | 29234 | 20365 | 8869 (182) | 2 | $-10946.59 | -6.0% |
| **+10¢ (15¢ stop)** | 63989 | 63883 | 106 (63) | 1 | $-23725.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 17:08 | +10 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-08 17:08 | +5 | NEAR | DOWN | 0.69 | 0.78 | 0.62 |
| 11-08 17:08 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-08 17:07 | +10 stop | ZEC | UP | 0.54 | 0.28 | -2.93 |
| 11-08 17:06 | +10 stop | HYPE | DOWN | 0.53 | 0.69 | 1.27 |
| 11-08 17:06 | +5 | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-08 17:06 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.00 |
| 11-08 17:03 | +10 stop | DOGE | UP | 0.62 | 0.76 | 1.10 |
| 11-08 17:03 | +20 | DOGE | UP | 0.62 | open |  |
| 11-08 17:03 | +15 | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 11-08 17:03 | +10 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 11-08 17:03 | +5 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 11-08 17:03 | +5 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-08 17:03 | +10 stop | ZEC | DOWN | 0.57 | 0.41 | -1.95 |
| 11-08 17:03 | +20 | ZEC | DOWN | 0.57 | 0.88 | 2.84 |
| 11-08 17:03 | +15 | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 11-08 17:03 | +10 | ZEC | DOWN | 0.56 | 0.70 | 1.07 |
| 11-08 17:03 | +5 | ZEC | DOWN | 0.56 | 0.63 | 0.40 |
| 11-08 17:02 | +10 stop | HYPE | UP | 0.55 | 0.39 | -1.95 |
| 11-08 17:02 | +20 | HYPE | UP | 0.55 | open |  |
| 11-08 17:02 | +15 | HYPE | UP | 0.55 | open |  |
| 11-08 17:02 | +10 | HYPE | UP | 0.55 | open |  |
| 11-08 17:02 | +5 | HYPE | UP | 0.55 | 0.63 | 0.45 |
| 11-08 17:02 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 11-08 17:01 | +10 stop | SOL | UP | 0.62 | 0.76 | 1.10 |
| 11-08 17:01 | +20 | SOL | UP | 0.62 | 0.85 | 2.04 |
| 11-08 17:01 | +15 | SOL | UP | 0.62 | 0.85 | 2.04 |
| 11-08 17:01 | +10 | SOL | UP | 0.62 | 0.76 | 1.10 |
| 11-08 17:01 | +5 | SOL | UP | 0.62 | 0.70 | 0.48 |
| 11-08 17:01 | +10 stop | BTC | UP | 0.67 | 0.81 | 1.13 |
| 11-08 17:01 | +20 | BTC | UP | 0.67 | 0.87 | 1.76 |
| 11-08 17:01 | +15 | BTC | UP | 0.67 | 0.83 | 1.34 |
| 11-08 17:01 | +10 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-08 17:01 | +5 | BTC | UP | 0.65 | 0.73 | 0.50 |
| 11-08 17:01 | +10 stop | BNB | UP | 0.64 | 0.75 | 0.79 |
| 11-08 17:01 | +20 | BNB | UP | 0.64 | 0.84 | 1.73 |
| 11-08 17:01 | +15 | BNB | UP | 0.64 | 0.80 | 1.31 |
| 11-08 17:01 | +10 | BNB | UP | 0.64 | 0.75 | 0.79 |
| 11-08 17:01 | +5 | BNB | UP | 0.64 | 0.70 | 0.28 |
| 11-08 17:01 | +10 stop | XRP | UP | 0.66 | 0.81 | 1.23 |
