# Range-Scalp Bot

*Updated Thu Nov 12 15:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57057 | 49737 | 7320 (101) | 1 | $-15707.80 | -4.4% |
| **+10¢** | 42647 | 34108 | 8539 (133) | 1 | $-14632.06 | -5.5% |
| **+15¢** | 35757 | 26568 | 9189 (167) | 1 | $-13215.52 | -5.9% |
| **+20¢** | 31854 | 22213 | 9641 (217) | 5 | $-11586.95 | -5.8% |
| **+10¢ (15¢ stop)** | 69577 | 69449 | 128 (78) | 1 | $-25701.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 15:05 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-12 15:05 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-12 15:05 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 11-12 15:05 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 15:05 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-12 15:05 | +10 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-12 15:05 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-12 15:05 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 11-12 15:05 | +5 | HYPE | DOWN | 0.67 | open |  |
| 11-12 15:01 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-12 15:01 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.74 |
| 11-12 15:01 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-12 15:01 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 11-12 15:01 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 15:01 | +5 | BNB | DOWN | 0.69 | 0.75 | 0.31 |
| 11-12 15:01 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 15:01 | +20 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 11-12 15:01 | +15 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-12 15:01 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 15:01 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-12 15:01 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 15:01 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-12 15:01 | +15 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-12 15:01 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 15:01 | +5 | NEAR | DOWN | 0.63 | 0.71 | 0.48 |
| 11-12 15:00 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 15:00 | +20 | ETH | DOWN | 0.69 | open |  |
| 11-12 15:00 | +15 | ETH | DOWN | 0.69 | 0.87 | 1.57 |
| 11-12 15:00 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 15:00 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 15:00 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 15:00 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-12 15:00 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 11-12 15:00 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-12 15:00 | +5 | SOL | DOWN | 0.68 | 0.76 | 0.51 |
| 11-12 15:00 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-12 15:00 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-12 15:00 | +15 | ZEC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-12 15:00 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-12 15:00 | +5 | ZEC | DOWN | 0.69 | 0.77 | 0.52 |
