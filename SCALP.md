# Range-Scalp Bot

*Updated Sat Nov 07 20:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51482 | 44891 | 6591 (80) | 2 | $-14270.43 | -4.4% |
| **+10¢** | 38415 | 30731 | 7684 (106) | 3 | $-13273.16 | -5.5% |
| **+15¢** | 32162 | 23881 | 8281 (135) | 4 | $-12172.31 | -6.0% |
| **+20¢** | 28608 | 19928 | 8680 (178) | 4 | $-10726.76 | -6.0% |
| **+10¢ (15¢ stop)** | 62684 | 62581 | 103 (61) | 1 | $-23173.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 20:18 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-07 20:18 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-07 20:18 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 20:18 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-07 20:18 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-07 20:18 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-07 20:18 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-07 20:18 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-07 20:17 | +10 stop | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-07 20:17 | +20 | HYPE | DOWN | 0.61 | open |  |
| 11-07 20:17 | +15 | HYPE | DOWN | 0.61 | open |  |
| 11-07 20:17 | +10 | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-07 20:17 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-07 20:17 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-07 20:17 | +20 | SOL | DOWN | 0.68 | 0.90 | 1.97 |
| 11-07 20:17 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-07 20:17 | +10 | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 11-07 20:17 | +5 | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 11-07 20:17 | +5 | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-07 20:16 | +10 stop | ETH | UP | 0.53 | 0.28 | -2.83 |
| 11-07 20:16 | +20 | ETH | UP | 0.53 | open |  |
| 11-07 20:16 | +15 | ETH | UP | 0.53 | open |  |
| 11-07 20:16 | +10 | ETH | UP | 0.53 | open |  |
| 11-07 20:16 | +5 | ETH | UP | 0.53 | open |  |
| 11-07 20:16 | +10 stop | XRP | UP | 0.51 | 0.33 | -2.14 |
| 11-07 20:16 | +20 | XRP | UP | 0.51 | open |  |
| 11-07 20:16 | +15 | XRP | UP | 0.51 | open |  |
| 11-07 20:16 | +10 | XRP | UP | 0.51 | open |  |
| 11-07 20:16 | +5 | XRP | UP | 0.51 | open |  |
| 11-07 20:16 | +10 stop | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-07 20:16 | +20 | DOGE | DOWN | 0.55 | 0.83 | 2.52 |
| 11-07 20:16 | +15 | DOGE | DOWN | 0.55 | 0.83 | 2.52 |
| 11-07 20:16 | +10 | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-07 20:16 | +5 | DOGE | DOWN | 0.55 | 0.60 | 0.15 |
| 11-07 20:16 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-07 20:16 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 11-07 20:16 | +15 | NEAR | DOWN | 0.60 | 0.79 | 1.61 |
| 11-07 20:16 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-07 20:16 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 11-07 20:16 | +10 stop | BNB | DOWN | 0.62 | 0.75 | 0.99 |
