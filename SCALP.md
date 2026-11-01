# Range-Scalp Bot

*Updated Sun Nov 01 03:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43157 | 37618 | 5539 (62) | 4 | $-12276.14 | -4.5% |
| **+10¢** | 32183 | 25783 | 6400 (84) | 6 | $-11000.04 | -5.4% |
| **+15¢** | 26925 | 20028 | 6897 (112) | 7 | $-10064.25 | -6.0% |
| **+20¢** | 23909 | 16683 | 7226 (146) | 8 | $-8899.06 | -5.9% |
| **+10¢ (15¢ stop)** | 52630 | 52547 | 83 (48) | 4 | $-19918.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 03:33 | +5 | DOGE | UP | 0.68 | open |  |
| 11-01 03:33 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-01 03:32 | +10 stop | ETH | DOWN | 0.48 | open |  |
| 11-01 03:32 | +20 | ETH | DOWN | 0.48 | open |  |
| 11-01 03:32 | +15 | ETH | DOWN | 0.49 | open |  |
| 11-01 03:32 | +10 | ETH | DOWN | 0.49 | open |  |
| 11-01 03:32 | +5 | ETH | DOWN | 0.49 | 0.54 | 0.14 |
| 11-01 03:31 | +10 stop | DOGE | UP | 0.58 | open |  |
| 11-01 03:31 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 03:31 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 11-01 03:31 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-01 03:31 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 03:31 | +5 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 03:31 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 11-01 03:31 | +20 | SOL | UP | 0.68 | open |  |
| 11-01 03:31 | +15 | SOL | UP | 0.68 | open |  |
| 11-01 03:31 | +10 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 11-01 03:31 | +5 | SOL | UP | 0.68 | 0.75 | 0.40 |
| 11-01 03:31 | +10 stop | BNB | UP | 0.53 | 0.72 | 1.57 |
| 11-01 03:31 | +20 | BNB | UP | 0.53 | open |  |
| 11-01 03:31 | +15 | BNB | UP | 0.53 | 0.72 | 1.57 |
| 11-01 03:31 | +10 | BNB | UP | 0.53 | 0.72 | 1.57 |
| 11-01 03:31 | +5 | BNB | UP | 0.53 | 0.59 | 0.25 |
| 11-01 03:31 | +5 | DOGE | UP | 0.57 | 0.64 | 0.35 |
| 11-01 03:31 | +10 stop | BTC | UP | 0.64 | open |  |
| 11-01 03:31 | +20 | BTC | UP | 0.64 | open |  |
| 11-01 03:31 | +15 | BTC | UP | 0.64 | open |  |
| 11-01 03:31 | +10 | BTC | UP | 0.64 | open |  |
| 11-01 03:31 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 11-01 03:31 | +10 stop | XRP | DOWN | 0.56 | 0.28 | -3.13 |
| 11-01 03:31 | +20 | XRP | DOWN | 0.56 | open |  |
| 11-01 03:31 | +15 | XRP | DOWN | 0.56 | open |  |
| 11-01 03:31 | +10 | XRP | DOWN | 0.56 | open |  |
| 11-01 03:31 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-01 03:31 | +10 stop | DOGE | DOWN | 0.54 | 0.37 | -2.05 |
| 11-01 03:31 | +20 | DOGE | DOWN | 0.54 | open |  |
| 11-01 03:31 | +15 | DOGE | DOWN | 0.54 | open |  |
| 11-01 03:31 | +10 | DOGE | DOWN | 0.54 | open |  |
| 11-01 03:31 | +5 | DOGE | DOWN | 0.54 | 0.59 | 0.15 |
| 11-01 03:30 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
