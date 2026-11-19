# Range-Scalp Bot

*Updated Thu Nov 19 23:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65455 | 57142 | 8313 (124) | 7 | $-17492.35 | -4.2% |
| **+10¢** | 48873 | 39151 | 9722 (165) | 8 | $-16277.35 | -5.3% |
| **+15¢** | 40985 | 30497 | 10488 (211) | 8 | $-14646.86 | -5.7% |
| **+20¢** | 36491 | 25471 | 11020 (266) | 8 | $-12979.74 | -5.7% |
| **+10¢ (15¢ stop)** | 79700 | 79536 | 164 (98) | 0 | $-29342.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 23:09 | +10 stop | XRP | DOWN | 0.47 | 0.73 | 2.28 |
| 11-19 23:09 | +10 stop | XRP | UP | 0.39 | 0.54 | 1.15 |
| 11-19 23:07 | +10 stop | XRP | DOWN | 0.54 | 0.34 | -2.34 |
| 11-19 23:07 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 11-19 23:06 | +10 stop | XRP | UP | 0.60 | 0.43 | -2.05 |
| 11-19 23:05 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 11-19 23:05 | +10 stop | BNB | DOWN | 0.65 | 0.47 | -2.14 |
| 11-19 23:05 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-19 23:05 | +10 stop | XRP | DOWN | 0.50 | 0.34 | -1.95 |
| 11-19 23:04 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-19 23:04 | +10 stop | SOL | DOWN | 0.71 | 0.51 | -2.33 |
| 11-19 23:04 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-19 23:04 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-19 23:03 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 23:03 | +5 | BTC | UP | 0.57 | open |  |
| 11-19 23:03 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.97 |
| 11-19 23:03 | +20 | BNB | UP | 0.64 | open |  |
| 11-19 23:03 | +15 | BNB | UP | 0.64 | open |  |
| 11-19 23:03 | +10 | BNB | UP | 0.64 | open |  |
| 11-19 23:03 | +5 | BNB | UP | 0.64 | open |  |
| 11-19 23:03 | +10 stop | XRP | UP | 0.69 | 0.51 | -2.13 |
| 11-19 23:03 | +20 | XRP | UP | 0.69 | open |  |
| 11-19 23:03 | +15 | XRP | UP | 0.69 | open |  |
| 11-19 23:03 | +10 | XRP | UP | 0.69 | open |  |
| 11-19 23:03 | +5 | XRP | UP | 0.69 | open |  |
| 11-19 23:02 | +5 | SOL | UP | 0.53 | 0.59 | 0.27 |
| 11-19 23:02 | +10 stop | BTC | UP | 0.55 | 0.30 | -2.83 |
| 11-19 23:02 | +20 | BTC | UP | 0.53 | open |  |
| 11-19 23:02 | +15 | BTC | UP | 0.57 | open |  |
| 11-19 23:02 | +10 | BTC | UP | 0.57 | open |  |
| 11-19 23:02 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 11-19 23:02 | +10 stop | HYPE | UP | 0.66 | 0.39 | -3.03 |
| 11-19 23:02 | +20 | HYPE | UP | 0.66 | open |  |
| 11-19 23:02 | +15 | HYPE | UP | 0.66 | open |  |
| 11-19 23:02 | +10 | HYPE | UP | 0.66 | open |  |
| 11-19 23:02 | +5 | HYPE | UP | 0.66 | open |  |
| 11-19 23:02 | +10 stop | ETH | DOWN | 0.48 | 0.59 | 0.75 |
| 11-19 23:02 | +20 | ETH | DOWN | 0.48 | 0.76 | 2.49 |
| 11-19 23:02 | +15 | ETH | DOWN | 0.48 | 0.76 | 2.49 |
| 11-19 23:02 | +10 | ETH | DOWN | 0.48 | 0.59 | 0.75 |
