# Range-Scalp Bot

*Updated Mon Nov 09 02:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53166 | 46359 | 6807 (85) | 0 | $-14677.27 | -4.4% |
| **+10¢** | 39695 | 31757 | 7938 (110) | 1 | $-13664.38 | -5.5% |
| **+15¢** | 33261 | 24710 | 8551 (141) | 2 | $-12465.68 | -6.0% |
| **+20¢** | 29587 | 20621 | 8966 (186) | 2 | $-10976.20 | -5.9% |
| **+10¢ (15¢ stop)** | 64747 | 64641 | 106 (63) | 1 | $-23982.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 02:16 | +10 stop | HYPE | DOWN | 0.48 | open |  |
| 11-09 02:16 | +20 | HYPE | DOWN | 0.48 | open |  |
| 11-09 02:16 | +15 | HYPE | DOWN | 0.48 | open |  |
| 11-09 02:16 | +10 | HYPE | DOWN | 0.48 | open |  |
| 11-09 02:16 | +5 | HYPE | DOWN | 0.48 | 0.53 | 0.14 |
| 11-09 02:16 | +10 stop | DOGE | DOWN | 0.41 | 0.54 | 0.95 |
| 11-09 02:16 | +20 | DOGE | DOWN | 0.41 | open |  |
| 11-09 02:16 | +15 | DOGE | DOWN | 0.41 | open |  |
| 11-09 02:16 | +10 | DOGE | DOWN | 0.41 | 0.54 | 0.95 |
| 11-09 02:16 | +5 | DOGE | DOWN | 0.41 | 0.54 | 0.95 |
| 11-09 02:11 | +10 stop | ZEC | DOWN | 0.57 | 0.77 | 1.69 |
| 11-09 02:11 | +10 stop | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 11-09 02:09 | +10 stop | NEAR | UP | 0.69 | 0.36 | -3.60 |
| 11-09 02:08 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 11-09 02:05 | +10 stop | ZEC | UP | 0.71 | 0.38 | -3.62 |
| 11-09 02:05 | +5 | ZEC | UP | 0.71 | no | -7.25 |
| 11-09 02:05 | +5 | ZEC | DOWN | 0.48 | 0.59 | 0.75 |
| 11-09 02:04 | +5 | ZEC | DOWN | 0.55 | 0.60 | 0.15 |
| 11-09 02:04 | +10 stop | HYPE | DOWN | 0.46 | 0.56 | 0.64 |
| 11-09 02:04 | +10 stop | NEAR | DOWN | 0.51 | 0.31 | -2.33 |
| 11-09 02:04 | +5 | DOGE | DOWN | 0.68 | yes | -6.96 |
| 11-09 02:03 | +10 stop | BNB | UP | 0.50 | 0.71 | 1.77 |
| 11-09 02:03 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 11-09 02:03 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
| 11-09 02:03 | +10 stop | ZEC | DOWN | 0.59 | 0.37 | -2.54 |
| 11-09 02:03 | +10 | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 11-09 02:03 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 11-09 02:02 | +10 stop | NEAR | DOWN | 0.68 | 0.51 | -2.04 |
| 11-09 02:02 | +20 | NEAR | DOWN | 0.68 | 0.92 | 2.13 |
| 11-09 02:02 | +15 | NEAR | DOWN | 0.69 | 0.92 | 2.04 |
| 11-09 02:02 | +10 | NEAR | DOWN | 0.69 | 0.92 | 2.04 |
| 11-09 02:02 | +5 | NEAR | DOWN | 0.69 | 0.78 | 0.62 |
| 11-09 02:02 | +5 | ZEC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-09 02:02 | +10 stop | ETH | DOWN | 0.60 | 0.42 | -2.15 |
| 11-09 02:02 | +10 stop | HYPE | DOWN | 0.66 | 0.46 | -2.34 |
| 11-09 02:02 | +20 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 11-09 02:02 | +15 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 11-09 02:02 | +10 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 11-09 02:02 | +5 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 11-09 02:01 | +10 stop | XRP | DOWN | 0.68 | 0.50 | -2.14 |
