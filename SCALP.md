# Range-Scalp Bot

*Updated Tue Nov 24 19:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70971 | 61943 | 9028 (155) | 0 | $-18939.50 | -4.2% |
| **+10¢** | 52945 | 42403 | 10542 (201) | 0 | $-17528.85 | -5.3% |
| **+15¢** | 44344 | 32991 | 11353 (258) | 0 | $-15603.38 | -5.6% |
| **+20¢** | 39482 | 27531 | 11951 (324) | 0 | $-13965.41 | -5.6% |
| **+10¢ (15¢ stop)** | 86405 | 86204 | 201 (121) | 0 | $-31752.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 19:37 | +10 stop | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-24 19:35 | +10 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-24 19:35 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-24 19:35 | +10 | ETH | UP | 0.66 | no | -6.76 |
| 11-24 19:35 | +5 | ETH | UP | 0.67 | no | -6.86 |
| 11-24 19:34 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 11-24 19:34 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 19:34 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.89 |
| 11-24 19:34 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-24 19:34 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 19:34 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 11-24 19:33 | +20 | BTC | DOWN | 0.57 | 0.82 | 2.21 |
| 11-24 19:33 | +15 | BTC | DOWN | 0.57 | 0.74 | 1.38 |
| 11-24 19:33 | +10 stop | ETH | DOWN | 0.59 | 0.36 | -2.64 |
| 11-24 19:33 | +15 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 11-24 19:33 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-24 19:32 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-24 19:32 | +10 stop | ZEC | UP | 0.70 | 0.51 | -2.23 |
| 11-24 19:32 | +5 | ZEC | UP | 0.69 | no | -7.05 |
| 11-24 19:32 | +10 stop | ETH | UP | 0.61 | 0.37 | -2.74 |
| 11-24 19:32 | +10 | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-24 19:32 | +5 | ETH | UP | 0.61 | 0.68 | 0.37 |
| 11-24 19:32 | +10 stop | BTC | UP | 0.59 | 0.44 | -1.85 |
| 11-24 19:32 | +10 | BTC | UP | 0.59 | no | -6.07 |
| 11-24 19:32 | +5 | BTC | UP | 0.59 | no | -6.07 |
| 11-24 19:31 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-24 19:31 | +20 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 11-24 19:31 | +15 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 11-24 19:31 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-24 19:31 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 11-24 19:31 | +10 stop | ETH | DOWN | 0.45 | 0.56 | 0.74 |
| 11-24 19:31 | +20 | ETH | DOWN | 0.45 | 0.70 | 2.17 |
| 11-24 19:31 | +15 | ETH | DOWN | 0.45 | 0.62 | 1.35 |
| 11-24 19:31 | +10 | ETH | DOWN | 0.45 | 0.56 | 0.74 |
| 11-24 19:31 | +5 | ETH | DOWN | 0.45 | 0.56 | 0.74 |
| 11-24 19:31 | +10 stop | BTC | DOWN | 0.40 | 0.56 | 1.25 |
| 11-24 19:31 | +20 | BTC | DOWN | 0.42 | 0.62 | 1.65 |
| 11-24 19:31 | +15 | BTC | DOWN | 0.45 | 0.62 | 1.35 |
| 11-24 19:31 | +10 | BTC | DOWN | 0.44 | 0.56 | 0.84 |
| 11-24 19:31 | +5 | BTC | DOWN | 0.44 | 0.56 | 0.84 |
