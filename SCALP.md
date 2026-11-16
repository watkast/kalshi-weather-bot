# Range-Scalp Bot

*Updated Mon Nov 16 23:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62398 | 54439 | 7959 (117) | 1 | $-16882.18 | -4.3% |
| **+10¢** | 46599 | 37286 | 9313 (159) | 1 | $-15757.20 | -5.4% |
| **+15¢** | 39044 | 28998 | 10046 (201) | 5 | $-14338.61 | -5.9% |
| **+20¢** | 34796 | 24259 | 10537 (256) | 6 | $-12540.72 | -5.7% |
| **+10¢ (15¢ stop)** | 75944 | 75788 | 156 (92) | 0 | $-28020.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 23:03 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
| 11-16 23:02 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 23:02 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 23:02 | +5 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 23:02 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 23:02 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 23:02 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 23:02 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 23:02 | +10 stop | NEAR | DOWN | 0.54 | 0.68 | 1.06 |
| 11-16 23:02 | +20 | NEAR | DOWN | 0.54 | open |  |
| 11-16 23:02 | +15 | NEAR | DOWN | 0.54 | open |  |
| 11-16 23:02 | +10 | NEAR | DOWN | 0.54 | 0.68 | 1.06 |
| 11-16 23:02 | +5 | NEAR | DOWN | 0.54 | 0.63 | 0.55 |
| 11-16 23:02 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-16 23:02 | +20 | BTC | DOWN | 0.56 | open |  |
| 11-16 23:02 | +15 | BTC | DOWN | 0.56 | 0.74 | 1.48 |
| 11-16 23:02 | +10 | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-16 23:02 | +5 | BTC | DOWN | 0.57 | 0.66 | 0.56 |
| 11-16 23:02 | +10 stop | HYPE | UP | 0.67 | 0.48 | -2.22 |
| 11-16 23:01 | +5 | HYPE | UP | 0.70 | open |  |
| 11-16 23:01 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 23:01 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-16 23:01 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-16 23:01 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 23:01 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-16 23:01 | +10 stop | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 23:01 | +20 | ETH | DOWN | 0.66 | open |  |
| 11-16 23:01 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-16 23:01 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-16 23:01 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 11-16 23:01 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-16 23:01 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-16 23:01 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-16 23:01 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-16 23:01 | +5 | SOL | DOWN | 0.67 | 0.75 | 0.50 |
| 11-16 23:01 | +10 stop | HYPE | DOWN | 0.51 | 0.33 | -2.14 |
| 11-16 23:01 | +20 | HYPE | DOWN | 0.51 | open |  |
| 11-16 23:01 | +15 | HYPE | DOWN | 0.51 | open |  |
| 11-16 23:01 | +10 | HYPE | DOWN | 0.51 | open |  |
| 11-16 23:01 | +5 | HYPE | DOWN | 0.51 | 0.60 | 0.55 |
