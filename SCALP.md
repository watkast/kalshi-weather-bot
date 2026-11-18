# Range-Scalp Bot

*Updated Wed Nov 18 02:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63451 | 55336 | 8115 (118) | 3 | $-17367.45 | -4.3% |
| **+10¢** | 47392 | 37897 | 9495 (159) | 4 | $-16277.26 | -5.5% |
| **+15¢** | 39731 | 29492 | 10239 (203) | 8 | $-14775.66 | -5.9% |
| **+20¢** | 35397 | 24653 | 10744 (258) | 8 | $-13025.70 | -5.9% |
| **+10¢ (15¢ stop)** | 77225 | 77067 | 158 (93) | 3 | $-28432.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 02:05 | +10 stop | ZEC | UP | 0.68 | 0.49 | -2.24 |
| 11-18 02:05 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 11-18 02:05 | +20 | NEAR | DOWN | 0.47 | open |  |
| 11-18 02:05 | +15 | NEAR | DOWN | 0.47 | open |  |
| 11-18 02:05 | +10 | NEAR | DOWN | 0.47 | open |  |
| 11-18 02:05 | +5 | NEAR | DOWN | 0.47 | 0.54 | 0.34 |
| 11-18 02:05 | +10 stop | BTC | UP | 0.58 | open |  |
| 11-18 02:05 | +20 | BTC | UP | 0.58 | open |  |
| 11-18 02:05 | +15 | BTC | UP | 0.57 | open |  |
| 11-18 02:05 | +10 | BTC | UP | 0.53 | 0.67 | 1.06 |
| 11-18 02:05 | +5 | BTC | UP | 0.53 | 0.61 | 0.45 |
| 11-18 02:04 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 11-18 02:04 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-18 02:04 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-18 02:04 | +5 | ETH | DOWN | 0.60 | open |  |
| 11-18 02:04 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 11-18 02:04 | +5 | ZEC | UP | 0.66 | open |  |
| 11-18 02:04 | +10 stop | BNB | DOWN | 0.48 | 0.63 | 1.15 |
| 11-18 02:04 | +15 | BNB | DOWN | 0.49 | open |  |
| 11-18 02:04 | +10 | BNB | DOWN | 0.51 | 0.63 | 0.85 |
| 11-18 02:04 | +5 | BNB | DOWN | 0.51 | 0.63 | 0.84 |
| 11-18 02:04 | +10 stop | DOGE | DOWN | 0.62 | 0.45 | -2.04 |
| 11-18 02:04 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-18 02:04 | +10 | DOGE | DOWN | 0.62 | open |  |
| 11-18 02:04 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-18 02:04 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-18 02:04 | +10 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-18 02:04 | +5 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-18 02:04 | +10 stop | ZEC | DOWN | 0.50 | 0.34 | -1.94 |
| 11-18 02:04 | +15 | ZEC | DOWN | 0.50 | open |  |
| 11-18 02:04 | +10 | ZEC | DOWN | 0.50 | open |  |
| 11-18 02:04 | +5 | ZEC | DOWN | 0.50 | 0.57 | 0.34 |
| 11-18 02:02 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-18 02:02 | +20 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-18 02:02 | +15 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-18 02:02 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-18 02:02 | +5 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-18 02:01 | +10 stop | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
| 11-18 02:01 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-18 02:01 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
