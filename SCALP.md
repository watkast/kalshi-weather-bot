# Range-Scalp Bot

*Updated Tue Nov 24 08:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70721 | 61730 | 8991 (148) | 2 | $-18896.78 | -4.2% |
| **+10¢** | 52755 | 42257 | 10498 (193) | 2 | $-17485.36 | -5.3% |
| **+15¢** | 44195 | 32887 | 11308 (250) | 2 | $-15562.67 | -5.6% |
| **+20¢** | 39355 | 27449 | 11906 (316) | 2 | $-13931.31 | -5.6% |
| **+10¢ (15¢ stop)** | 86103 | 85905 | 198 (118) | 2 | $-31645.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 08:46 | +10 stop | NEAR | UP | 0.66 | open |  |
| 11-24 08:46 | +20 | NEAR | UP | 0.66 | open |  |
| 11-24 08:46 | +15 | NEAR | UP | 0.68 | open |  |
| 11-24 08:46 | +10 | NEAR | UP | 0.68 | open |  |
| 11-24 08:46 | +5 | NEAR | UP | 0.68 | open |  |
| 11-24 08:46 | +10 stop | SOL | UP | 0.70 | open |  |
| 11-24 08:46 | +20 | SOL | UP | 0.70 | open |  |
| 11-24 08:46 | +15 | SOL | UP | 0.70 | open |  |
| 11-24 08:46 | +10 | SOL | UP | 0.70 | open |  |
| 11-24 08:46 | +5 | SOL | UP | 0.70 | open |  |
| 11-24 08:40 | +10 stop | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-24 08:40 | +15 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-24 08:40 | +10 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-24 08:40 | +5 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-24 08:40 | +10 | XRP | DOWN | 0.62 | yes | -6.37 |
| 11-24 08:40 | +5 | XRP | DOWN | 0.62 | yes | -6.37 |
| 11-24 08:40 | +10 stop | DOGE | UP | 0.70 | 0.88 | 1.59 |
| 11-24 08:39 | +10 stop | HYPE | UP | 0.50 | 0.68 | 1.46 |
| 11-24 08:38 | +10 stop | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-24 08:38 | +5 | BNB | UP | 0.69 | 0.79 | 0.68 |
| 11-24 08:38 | +10 stop | BTC | UP | 0.55 | 0.78 | 1.99 |
| 11-24 08:38 | +10 | BTC | UP | 0.55 | 0.78 | 1.99 |
| 11-24 08:38 | +5 | BTC | UP | 0.55 | 0.78 | 1.99 |
| 11-24 08:38 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 11-24 08:38 | +10 stop | ETH | UP | 0.56 | 0.75 | 1.58 |
| 11-24 08:37 | +10 stop | DOGE | UP | 0.59 | 0.73 | 1.09 |
| 11-24 08:37 | +10 stop | NEAR | DOWN | 0.44 | 0.54 | 0.64 |
| 11-24 08:37 | +10 stop | SOL | DOWN | 0.64 | 0.40 | -2.74 |
| 11-24 08:37 | +10 stop | XRP | DOWN | 0.68 | 0.48 | -2.34 |
| 11-24 08:37 | +5 | BNB | UP | 0.52 | 0.57 | 0.14 |
| 11-24 08:36 | +10 stop | HYPE | UP | 0.64 | 0.44 | -2.35 |
| 11-24 08:36 | +10 stop | NEAR | UP | 0.66 | 0.46 | -2.34 |
| 11-24 08:36 | +10 | NEAR | UP | 0.66 | 0.83 | 1.44 |
| 11-24 08:36 | +5 | NEAR | UP | 0.66 | 0.75 | 0.60 |
| 11-24 08:36 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 11-24 08:35 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 11-24 08:35 | +10 stop | HYPE | UP | 0.54 | 0.67 | 0.96 |
| 11-24 08:34 | +10 stop | ETH | DOWN | 0.53 | 0.33 | -2.36 |
| 11-24 08:34 | +10 stop | XRP | DOWN | 0.59 | 0.43 | -1.95 |
| 11-24 08:34 | +10 stop | BNB | UP | 0.65 | 0.49 | -1.94 |
