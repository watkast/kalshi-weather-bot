# Range-Scalp Bot

*Updated Tue Oct 06 02:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4499 | 3880 | 619 (6) | 1 | $-1508.03 | -5.3% |
| **+10¢** | 3465 | 2746 | 719 (9) | 2 | $-1402.06 | -6.4% |
| **+15¢** | 2906 | 2147 | 759 (12) | 3 | $-1212.11 | -6.6% |
| **+20¢** | 2602 | 1812 | 790 (17) | 6 | $-1016.60 | -6.2% |
| **+10¢ (15¢ stop)** | 5529 | 5518 | 11 (6) | 1 | $-2006.55 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 02:06 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-06 02:06 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-06 02:06 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 10-06 02:03 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-06 02:02 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 10-06 02:02 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-06 02:02 | +15 | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 10-06 02:02 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 10-06 02:02 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 10-06 02:02 | +10 stop | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-06 02:02 | +20 | HYPE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-06 02:02 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-06 02:02 | +10 | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-06 02:02 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-06 02:01 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-06 02:01 | +20 | ETH | DOWN | 0.69 | open |  |
| 10-06 02:01 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-06 02:01 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-06 02:01 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-06 02:01 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-06 02:01 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-06 02:01 | +15 | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-06 02:01 | +10 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-06 02:01 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-06 02:01 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-06 02:01 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-06 02:01 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-06 02:01 | +10 | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-06 02:01 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-06 02:01 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.90 |
| 10-06 02:01 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.90 |
| 10-06 02:01 | +5 | ZEC | DOWN | 0.61 | 0.73 | 0.90 |
| 10-06 02:00 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-06 02:00 | +20 | XRP | DOWN | 0.71 | 0.91 | 1.79 |
| 10-06 02:00 | +15 | XRP | DOWN | 0.71 | 0.91 | 1.79 |
| 10-06 02:00 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-06 02:00 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 10-06 02:00 | +10 stop | BNB | UP | 0.57 | 0.33 | -2.74 |
| 10-06 02:00 | +20 | BNB | UP | 0.57 | open |  |
| 10-06 02:00 | +15 | BNB | UP | 0.57 | open |  |
