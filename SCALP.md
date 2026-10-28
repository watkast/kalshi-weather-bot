# Range-Scalp Bot

*Updated Wed Oct 28 12:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38066 | 33208 | 4858 (46) | 0 | $-10759.81 | -4.5% |
| **+10¢** | 28401 | 22783 | 5618 (68) | 0 | $-9607.06 | -5.4% |
| **+15¢** | 23764 | 17733 | 6031 (93) | 0 | $-8551.86 | -5.7% |
| **+20¢** | 21076 | 14761 | 6315 (118) | 1 | $-7525.58 | -5.7% |
| **+10¢ (15¢ stop)** | 46607 | 46540 | 67 (35) | 0 | $-17748.96 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 12:04 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 12:04 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 12:04 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-28 12:02 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.94 |
| 10-28 12:02 | +20 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 10-28 12:02 | +15 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 10-28 12:02 | +10 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 10-28 12:02 | +5 | NEAR | DOWN | 0.68 | 0.86 | 1.55 |
| 10-28 12:02 | +10 stop | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-28 12:02 | +15 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-28 12:02 | +10 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-28 12:02 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 10-28 12:01 | +10 stop | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 10-28 12:01 | +20 | DOGE | DOWN | 0.69 | 0.92 | 2.09 |
| 10-28 12:01 | +15 | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 10-28 12:01 | +10 | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 10-28 12:01 | +5 | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 10-28 12:01 | +10 stop | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-28 12:01 | +20 | BTC | DOWN | 0.64 | 0.90 | 2.39 |
| 10-28 12:01 | +15 | BTC | DOWN | 0.64 | 0.83 | 1.63 |
| 10-28 12:01 | +10 | BTC | DOWN | 0.64 | 0.83 | 1.63 |
| 10-28 12:01 | +5 | BTC | DOWN | 0.64 | 0.83 | 1.63 |
| 10-28 12:01 | +10 stop | BNB | UP | 0.48 | 0.63 | 1.15 |
| 10-28 12:01 | +20 | BNB | UP | 0.48 | open |  |
| 10-28 12:01 | +15 | BNB | UP | 0.48 | 0.63 | 1.15 |
| 10-28 12:01 | +10 | BNB | UP | 0.48 | 0.63 | 1.15 |
| 10-28 12:01 | +5 | BNB | UP | 0.48 | 0.63 | 1.15 |
| 10-28 12:01 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 12:01 | +20 | ZEC | DOWN | 0.63 | 0.87 | 2.15 |
| 10-28 12:01 | +15 | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-28 12:01 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 12:01 | +5 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 12:01 | +10 stop | SOL | DOWN | 0.60 | 0.80 | 1.71 |
| 10-28 12:01 | +20 | SOL | DOWN | 0.61 | 0.88 | 2.45 |
| 10-28 12:01 | +15 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 10-28 12:01 | +10 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 10-28 12:01 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-28 12:01 | +10 stop | ETH | DOWN | 0.62 | 0.91 | 2.69 |
| 10-28 12:01 | +20 | ETH | DOWN | 0.62 | 0.91 | 2.69 |
| 10-28 12:01 | +15 | ETH | DOWN | 0.63 | 0.91 | 2.59 |
