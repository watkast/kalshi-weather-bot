# Range-Scalp Bot

*Updated Tue Nov 10 02:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54188 | 47275 | 6913 (89) | 1 | $-14720.61 | -4.3% |
| **+10¢** | 40480 | 32412 | 8068 (117) | 3 | $-13674.31 | -5.4% |
| **+15¢** | 33927 | 25232 | 8695 (149) | 4 | $-12427.65 | -5.8% |
| **+20¢** | 30209 | 21090 | 9119 (195) | 4 | $-10834.10 | -5.7% |
| **+10¢ (15¢ stop)** | 66011 | 65901 | 110 (66) | 3 | $-24412.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 02:35 | +5 | BNB | DOWN | 0.70 | open |  |
| 11-10 02:32 | +10 stop | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-10 02:32 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-10 02:32 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-10 02:32 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-10 02:32 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-10 02:32 | +10 stop | HYPE | DOWN | 0.66 | open |  |
| 11-10 02:32 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-10 02:32 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-10 02:32 | +15 | BNB | DOWN | 0.65 | open |  |
| 11-10 02:32 | +10 | BNB | DOWN | 0.65 | open |  |
| 11-10 02:32 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 11-10 02:31 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-10 02:31 | +20 | BTC | DOWN | 0.68 | open |  |
| 11-10 02:31 | +15 | BTC | DOWN | 0.68 | open |  |
| 11-10 02:31 | +10 | BTC | DOWN | 0.68 | open |  |
| 11-10 02:31 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-10 02:31 | +20 | HYPE | DOWN | 0.69 | open |  |
| 11-10 02:31 | +15 | HYPE | DOWN | 0.69 | open |  |
| 11-10 02:31 | +10 | HYPE | DOWN | 0.69 | open |  |
| 11-10 02:31 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-10 02:28 | +10 stop | SOL | DOWN | 0.24 | 0.54 | 2.69 |
| 11-10 02:28 | +20 | SOL | DOWN | 0.26 | 0.54 | 2.48 |
| 11-10 02:28 | +15 | SOL | DOWN | 0.26 | 0.54 | 2.48 |
| 11-10 02:28 | +10 | SOL | DOWN | 0.25 | 0.54 | 2.58 |
| 11-10 02:28 | +5 | SOL | DOWN | 0.26 | 0.54 | 2.48 |
| 11-10 02:21 | +5 | SOL | DOWN | 0.66 | 0.75 | 0.60 |
| 11-10 02:20 | +10 stop | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-10 02:17 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-10 02:17 | +20 | BTC | DOWN | 0.66 | 0.91 | 2.22 |
| 11-10 02:17 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-10 02:17 | +10 | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 11-10 02:17 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 11-10 02:17 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.75 |
| 11-10 02:17 | +20 | BNB | DOWN | 0.67 | 0.90 | 2.11 |
| 11-10 02:17 | +15 | BNB | DOWN | 0.67 | 0.86 | 1.68 |
| 11-10 02:17 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.75 |
| 11-10 02:17 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.22 |
| 11-10 02:17 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 02:17 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
