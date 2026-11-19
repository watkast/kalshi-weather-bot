# Range-Scalp Bot

*Updated Thu Nov 19 05:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64773 | 56523 | 8250 (124) | 5 | $-17480.92 | -4.3% |
| **+10¢** | 48393 | 38740 | 9653 (165) | 6 | $-16290.64 | -5.4% |
| **+15¢** | 40581 | 30171 | 10410 (210) | 7 | $-14716.09 | -5.8% |
| **+20¢** | 36138 | 25206 | 10932 (265) | 7 | $-13021.24 | -5.7% |
| **+10¢ (15¢ stop)** | 78796 | 78632 | 164 (98) | 4 | $-28895.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 05:07 | +10 stop | ETH | UP | 0.62 | open |  |
| 11-19 05:07 | +5 | ETH | UP | 0.68 | open |  |
| 11-19 05:07 | +10 stop | BTC | DOWN | 0.50 | open |  |
| 11-19 05:06 | +10 stop | BNB | UP | 0.66 | open |  |
| 11-19 05:06 | +5 | BNB | UP | 0.64 | open |  |
| 11-19 05:06 | +10 stop | BNB | DOWN | 0.52 | 0.64 | 0.85 |
| 11-19 05:06 | +5 | BNB | DOWN | 0.52 | 0.64 | 0.85 |
| 11-19 05:06 | +10 stop | ETH | DOWN | 0.48 | 0.30 | -2.13 |
| 11-19 05:06 | +15 | ETH | DOWN | 0.48 | open |  |
| 11-19 05:06 | +10 | ETH | DOWN | 0.48 | open |  |
| 11-19 05:06 | +5 | ETH | DOWN | 0.48 | 0.57 | 0.54 |
| 11-19 05:06 | +10 stop | NEAR | DOWN | 0.55 | open |  |
| 11-19 05:06 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-19 05:06 | +10 | BTC | DOWN | 0.71 | open |  |
| 11-19 05:06 | +5 | BTC | DOWN | 0.71 | open |  |
| 11-19 05:06 | +10 stop | ZEC | UP | 0.57 | 0.79 | 1.90 |
| 11-19 05:06 | +5 | ZEC | UP | 0.57 | 0.79 | 1.90 |
| 11-19 05:05 | +10 stop | SOL | UP | 0.58 | 0.69 | 0.77 |
| 11-19 05:05 | +10 stop | BTC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-19 05:03 | +10 stop | NEAR | DOWN | 0.61 | 0.42 | -2.25 |
| 11-19 05:03 | +10 | NEAR | DOWN | 0.61 | open |  |
| 11-19 05:02 | +5 | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-19 05:02 | +5 | ZEC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-19 05:02 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-19 05:01 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-19 05:01 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-19 05:01 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-19 05:01 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.84 |
| 11-19 05:01 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.33 |
| 11-19 05:01 | +10 stop | BNB | DOWN | 0.67 | 0.50 | -2.04 |
| 11-19 05:01 | +20 | BNB | DOWN | 0.67 | open |  |
| 11-19 05:01 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-19 05:01 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-19 05:01 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
| 11-19 05:01 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-19 05:01 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 11-19 05:01 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 11-19 05:01 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-19 05:01 | +5 | XRP | DOWN | 0.65 | 0.74 | 0.60 |
| 11-19 05:01 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.85 |
