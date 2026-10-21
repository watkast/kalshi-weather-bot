# Range-Scalp Bot

*Updated Wed Oct 21 08:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26876 | 23398 | 3478 (39) | 5 | $-7848.53 | -4.6% |
| **+10¢** | 20222 | 16204 | 4018 (55) | 5 | $-6941.35 | -5.5% |
| **+15¢** | 16931 | 12613 | 4318 (78) | 5 | $-6164.24 | -5.8% |
| **+20¢** | 14989 | 10462 | 4527 (97) | 6 | $-5544.75 | -5.9% |
| **+10¢ (15¢ stop)** | 32963 | 32904 | 59 (32) | 0 | $-12189.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 08:10 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-21 08:08 | +10 stop | ZEC | UP | 0.50 | 0.27 | -2.62 |
| 10-21 08:08 | +5 | ZEC | UP | 0.48 | 0.58 | 0.64 |
| 10-21 08:08 | +10 stop | BTC | UP | 0.66 | 0.48 | -2.14 |
| 10-21 08:08 | +5 | BTC | UP | 0.66 | open |  |
| 10-21 08:07 | +10 stop | ZEC | DOWN | 0.48 | 0.33 | -1.86 |
| 10-21 08:07 | +10 | ZEC | DOWN | 0.48 | 0.70 | 1.84 |
| 10-21 08:07 | +5 | ZEC | DOWN | 0.48 | 0.56 | 0.42 |
| 10-21 08:06 | +10 stop | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 10-21 08:06 | +10 stop | BTC | DOWN | 0.59 | 0.34 | -2.83 |
| 10-21 08:05 | +10 stop | NEAR | DOWN | 0.49 | 0.60 | 0.75 |
| 10-21 08:05 | +5 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-21 08:05 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-21 08:04 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-21 08:03 | +10 stop | NEAR | UP | 0.61 | 0.41 | -2.34 |
| 10-21 08:03 | +5 | ZEC | DOWN | 0.49 | 0.61 | 0.85 |
| 10-21 08:03 | +10 stop | BTC | DOWN | 0.40 | 0.56 | 1.25 |
| 10-21 08:03 | +10 stop | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 10-21 08:03 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 10-21 08:03 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-21 08:03 | +10 stop | XRP | DOWN | 0.69 | 0.47 | -2.53 |
| 10-21 08:03 | +20 | XRP | DOWN | 0.69 | 0.90 | 1.90 |
| 10-21 08:03 | +15 | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 10-21 08:03 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 10-21 08:03 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-21 08:02 | +10 stop | ETH | UP | 0.67 | 0.41 | -2.93 |
| 10-21 08:02 | +20 | ETH | UP | 0.67 | open |  |
| 10-21 08:02 | +15 | ETH | UP | 0.67 | open |  |
| 10-21 08:02 | +10 | ETH | UP | 0.67 | open |  |
| 10-21 08:02 | +5 | ETH | UP | 0.67 | open |  |
| 10-21 08:02 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-21 08:02 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-21 08:02 | +15 | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 10-21 08:02 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-21 08:02 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-21 08:02 | +10 stop | BNB | UP | 0.70 | 0.40 | -3.29 |
| 10-21 08:02 | +20 | BNB | UP | 0.70 | open |  |
| 10-21 08:02 | +15 | BNB | UP | 0.70 | open |  |
| 10-21 08:02 | +10 | BNB | UP | 0.70 | open |  |
| 10-21 08:02 | +5 | BNB | UP | 0.70 | open |  |
