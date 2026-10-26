# Range-Scalp Bot

*Updated Mon Oct 26 04:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34265 | 29919 | 4346 (43) | 7 | $-9454.27 | -4.4% |
| **+10¢** | 25644 | 20613 | 5031 (65) | 7 | $-8322.03 | -5.2% |
| **+15¢** | 21445 | 16028 | 5417 (89) | 7 | $-7447.51 | -5.5% |
| **+20¢** | 19010 | 13338 | 5672 (111) | 7 | $-6518.57 | -5.5% |
| **+10¢ (15¢ stop)** | 41984 | 41922 | 62 (33) | 0 | $-15994.75 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 04:52 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-26 04:51 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 10-26 04:50 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-26 04:50 | +10 stop | SOL | UP | 0.65 | 0.78 | 1.01 |
| 10-26 04:49 | +10 stop | XRP | UP | 0.54 | 0.78 | 2.09 |
| 10-26 04:49 | +5 | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-26 04:49 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-26 04:49 | +15 | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 10-26 04:49 | +10 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-26 04:49 | +10 stop | NEAR | DOWN | 0.57 | 0.31 | -2.92 |
| 10-26 04:48 | +10 stop | ZEC | DOWN | 0.68 | 0.42 | -2.94 |
| 10-26 04:48 | +10 stop | ETH | UP | 0.55 | 0.67 | 0.86 |
| 10-26 04:48 | +10 stop | SOL | UP | 0.60 | 0.72 | 0.88 |
| 10-26 04:47 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 10-26 04:47 | +10 stop | BNB | UP | 0.54 | 0.68 | 1.06 |
| 10-26 04:47 | +20 | BNB | UP | 0.54 | 0.80 | 2.30 |
| 10-26 04:47 | +15 | BNB | UP | 0.54 | 0.80 | 2.30 |
| 10-26 04:47 | +10 | BNB | UP | 0.54 | 0.68 | 1.06 |
| 10-26 04:47 | +5 | BNB | UP | 0.54 | 0.61 | 0.35 |
| 10-26 04:47 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 10-26 04:47 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-26 04:47 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-26 04:47 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-26 04:47 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-26 04:46 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-26 04:46 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-26 04:46 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-26 04:46 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-26 04:46 | +5 | BTC | DOWN | 0.59 | open |  |
| 10-26 04:46 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
| 10-26 04:46 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-26 04:46 | +15 | DOGE | DOWN | 0.59 | open |  |
| 10-26 04:46 | +10 | DOGE | DOWN | 0.59 | open |  |
| 10-26 04:46 | +5 | DOGE | DOWN | 0.59 | open |  |
| 10-26 04:46 | +10 stop | ETH | DOWN | 0.59 | 0.40 | -2.24 |
| 10-26 04:46 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-26 04:46 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-26 04:46 | +10 | ETH | DOWN | 0.59 | open |  |
| 10-26 04:46 | +5 | ETH | DOWN | 0.59 | open |  |
| 10-26 04:46 | +10 stop | ZEC | DOWN | 0.69 | 0.54 | -1.83 |
