# Range-Scalp Bot

*Updated Wed Oct 21 18:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27555 | 23995 | 3560 (39) | 6 | $-8029.47 | -4.6% |
| **+10¢** | 20716 | 16604 | 4112 (55) | 6 | $-7090.14 | -5.4% |
| **+15¢** | 17350 | 12925 | 4425 (78) | 6 | $-6330.12 | -5.8% |
| **+20¢** | 15358 | 10721 | 4637 (98) | 6 | $-5676.27 | -5.9% |
| **+10¢ (15¢ stop)** | 33813 | 33754 | 59 (32) | 0 | $-12579.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 18:12 | +10 stop | SOL | DOWN | 0.60 | 0.73 | 0.99 |
| 10-21 18:12 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 10-21 18:11 | +10 stop | SOL | UP | 0.43 | 0.54 | 0.74 |
| 10-21 18:11 | +10 stop | NEAR | UP | 0.40 | 0.63 | 1.96 |
| 10-21 18:11 | +10 stop | ETH | UP | 0.48 | 0.65 | 1.36 |
| 10-21 18:11 | +10 stop | BTC | UP | 0.71 | 0.48 | -2.63 |
| 10-21 18:11 | +10 | BTC | UP | 0.71 | open |  |
| 10-21 18:11 | +5 | BTC | UP | 0.71 | open |  |
| 10-21 18:10 | +10 stop | NEAR | DOWN | 0.65 | 0.39 | -2.93 |
| 10-21 18:10 | +10 stop | HYPE | UP | 0.63 | 0.81 | 1.50 |
| 10-21 18:10 | +10 stop | ETH | UP | 0.60 | 0.45 | -1.85 |
| 10-21 18:09 | +10 stop | ETH | DOWN | 0.53 | 0.33 | -2.34 |
| 10-21 18:08 | +10 stop | SOL | UP | 0.68 | 0.46 | -2.54 |
| 10-21 18:08 | +15 | SOL | UP | 0.68 | open |  |
| 10-21 18:08 | +10 | SOL | UP | 0.68 | open |  |
| 10-21 18:08 | +5 | SOL | UP | 0.67 | open |  |
| 10-21 18:08 | +10 stop | NEAR | UP | 0.62 | 0.45 | -2.05 |
| 10-21 18:08 | +15 | NEAR | UP | 0.62 | open |  |
| 10-21 18:08 | +10 | NEAR | UP | 0.62 | open |  |
| 10-21 18:08 | +5 | NEAR | UP | 0.62 | open |  |
| 10-21 18:08 | +10 stop | BTC | UP | 0.66 | 0.77 | 0.81 |
| 10-21 18:08 | +10 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 10-21 18:08 | +5 | BTC | UP | 0.66 | 0.74 | 0.50 |
| 10-21 18:07 | +10 stop | ETH | UP | 0.69 | 0.47 | -2.53 |
| 10-21 18:06 | +5 | BNB | UP | 0.47 | 0.64 | 1.35 |
| 10-21 18:05 | +10 stop | BNB | UP | 0.63 | 0.46 | -2.05 |
| 10-21 18:05 | +5 | ZEC | DOWN | 0.59 | 0.66 | 0.34 |
| 10-21 18:04 | +5 | ZEC | DOWN | 0.57 | 0.64 | 0.32 |
| 10-21 18:04 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-21 18:04 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.95 |
| 10-21 18:03 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 10-21 18:03 | +10 stop | BNB | UP | 0.64 | 0.49 | -1.85 |
| 10-21 18:03 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 10-21 18:03 | +10 stop | ZEC | UP | 0.53 | 0.37 | -1.95 |
| 10-21 18:03 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-21 18:02 | +10 stop | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-21 18:02 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 10-21 18:02 | +20 | BTC | UP | 0.69 | open |  |
| 10-21 18:02 | +15 | BTC | UP | 0.69 | open |  |
| 10-21 18:02 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
